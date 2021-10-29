# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Marcos Pereira <marcospereira.mpj@gmail.com>
# Modified by Sairam Krish <haisairam@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
from django.conf import settings
from django.http.response import JsonResponse
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakInvalidTokenError
from rest_framework.exceptions import PermissionDenied


logger = logging.getLogger(__name__)

def get_permissions(self, token, method_token_info='introspect', **kwargs):
    """
    Get permission by user token

    :param token: user token
    :param method_token_info: Decode token method
    :param kwargs: parameters for decode
    :return: permissions list
    """

    if not self.authorization.policies:
        raise Exception(
            "Keycloak settings not found. Load Authorization Keycloak settings." # noqa
        )

    token_info = self._token_info(token, method_token_info, **kwargs)

    if method_token_info == 'introspect' and not token_info['active']:
        raise KeycloakInvalidTokenError(
            "Token expired or invalid."
        )

    user_resources = token_info['resource_access'].get(self.client_id)
    if not user_resources:
        return None

    permissions = []

    for policy_name, policy in self.authorization.policies.items():
        for role in user_resources['roles']:
            policy_roles = [item.name for item in policy.roles]
            if role in policy_roles:
                permissions += policy.permissions

    return list(set(permissions))


KeycloakOpenID.get_permissions = get_permissions


class KeycloakMiddleware(object):

    header_key = "HTTP_AUTHORIZATION"
    set_session_state_cookie = True

    def __init__(self, get_response):

        self.config = settings.KEYCLOAK_CONFIG

        # Read configurations
        try:
            self.server_url = self.config['KEYCLOAK_SERVER_URL']
            self.client_id = self.config['KEYCLOAK_CLIENT_ID']
            self.realm = self.config['KEYCLOAK_REALM']
        except KeyError:
            raise Exception("KEYCLOAK_SERVER_URL, KEYCLOAK_CLIENT_ID or KEYCLOAK_REALM not found.") # noqa

        self.client_secret_key = self.config.get(
            'KEYCLOAK_CLIENT_SECRET_KEY', None)
        self.client_public_key = self.config.get(
            'KEYCLOAK_CLIENT_PUBLIC_KEY', None)
        self.default_access = self.config.get(
            'KEYCLOAK_DEFAULT_ACCESS', "DENY")
        self.method_validate_token = self.config.get(
            'KEYCLOAK_METHOD_VALIDATE_TOKEN', "INTROSPECT")
        self.keycloak_authorization_config = self.config.get(
            'KEYCLOAK_AUTHORIZATION_CONFIG', None)

        # Create Keycloak instance
        self.keycloak = KeycloakOpenID(server_url=self.server_url,
                                       client_id=self.client_id,
                                       realm_name=self.realm,
                                       client_secret_key=self.client_secret_key) # noqa

        # Read policies
        if self.keycloak_authorization_config:
            self.keycloak.load_authorization_config(
                self.keycloak_authorization_config)

        # Django
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Validate only the token introspect.
        :param request: django request
        :param view_func: view function
        :param view_args: view args
        :param view_kwargs: view kwargs
        :return: JSON response or None
        """

        # Load permissions from Keycloak
        keycloak_permissions = self.get_keycloak_permissions(request)

        # Set permissions for anonymous user
        if keycloak_permissions is None:
            keycloak_permissions = {
                'authority:view',
                'fond:view',
                'institution:view',
            }

        # Build Django permissions
        request.user._perm_cache = {
            'keycloak.%s' % perm.replace(':', '_')
            for perm in keycloak_permissions
        }

        # Extract required Keycloak permissions from view
        try:
            view_scopes = view_func.cls.keycloak_scopes
        except AttributeError:
            logger.debug('Allowing free access, since no authorization configuration (keycloak_scopes) found for this request route :%s', request) # noqa
            return None

        # Get DEFAULT required permission if method is not defined
        required_permission = view_scopes.get(request.method, None) \
            or view_scopes.get('DEFAULT', None)

        # DEFAULT scope not found and DEFAULT_ACCESS is DENY
        if not required_permission and self.default_access == 'DENY':
            return JsonResponse(
                {'detail': PermissionDenied.default_detail},
                status=PermissionDenied.status_code,
            )

        # Check required permission from user Keycloak permissions
        if required_permission not in keycloak_permissions:
            return JsonResponse(
                {'detail': PermissionDenied.default_detail},
                status=PermissionDenied.status_code,
            )

    def get_keycloak_permissions(self, request):
        """
        Extract permissions from Keycloak for current user.
        :param request: django request
        :return: set of permissions (as string) or None for anonymous user
        """

        # Get session token
        access_token = request.session.get('oidc_access_token', '')
        if not access_token:
            try:
                access_token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
            except:
                return None

        # No token is anonymous user: unknown permissions
        if not access_token:
            return None

        # Get permissions from Keycloak
        try:
            permissions = self.keycloak.get_permissions(access_token)
        except KeycloakInvalidTokenError:
            return None

        # Extract permissions from scopes
        return {p for perm in permissions for p in perm.scopes}
