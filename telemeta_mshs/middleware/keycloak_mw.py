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

import re
import logging
import requests
from django.conf import settings
from django.http.response import JsonResponse
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakInvalidTokenError
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mozilla_django_oidc.utils import absolutify, import_from_settings
from django.utils.crypto import get_random_string
from urllib import urlencode


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

    def __init__(self):
        """
        :param get_response:
        """

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
        # self.get_response = get_response

    @property
    def keycloak(self):
        return self._keycloak

    @keycloak.setter
    def keycloak(self, value):
        self._keycloak = value

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value

    @property
    def server_url(self):
        return self._server_url

    @server_url.setter
    def server_url(self, value):
        self._server_url = value

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def client_secret_key(self):
        return self._client_secret_key

    @client_secret_key.setter
    def client_secret_key(self, value):
        self._client_secret_key = value

    @property
    def client_public_key(self):
        return self._client_public_key

    @client_public_key.setter
    def client_public_key(self, value):
        self._client_public_key = value

    @property
    def realm(self):
        return self._realm

    @realm.setter
    def realm(self, value):
        self._realm = value

    @property
    def keycloak_authorization_config(self):
        return self._keycloak_authorization_config

    @keycloak_authorization_config.setter
    def keycloak_authorization_config(self, value):
        self._keycloak_authorization_config = value

    @property
    def method_validate_token(self):
        return self._method_validate_token

    @method_validate_token.setter
    def method_validate_token(self, value):
        self._method_validate_token = value

    # def __call__(self, request):
    #    """
    #    :param request:
    #    :return:
    #    """
    #    return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Validate only the token introspect.
        :param request: django request
        :param view_func:
        :param view_args: view args
        :param view_kwargs: view kwargs
        :return:
        """

        # Is there some exempts paths ?
        if hasattr(settings, 'KEYCLOAK_BEARER_AUTHENTICATION_EXEMPT_PATHS'):
            path = request.path_info.lstrip('/')

            # Search every KEYCLOAK_BEARER_AUTHENTICATION_EXEMPT_PATHS in path
            if any(re.match(m, path) for m in
                   settings.KEYCLOAK_BEARER_AUTHENTICATION_EXEMPT_PATHS):
                logger.debug('** exclude path found, skipping')
                return None

            # Exclude every URL pointing to the API service,
            #   for a list queryset.
            expr = re.compile("^api/[a-z0-9_]*/$")
            if expr.match(path):
                logger.debug('** exclude path : display template')
                return None

            # Exclude every URL pointing to the API service,
            #   for a detail queryset.
            expr = re.compile("^api/[a-z0-9_]*/[0-9]*/(complete/|)$")
            if expr.match(path):
                logger.debug('** exclude path : display template')
                return None

            # Exclude every URL pointing to the API service,
            #   for authenticate
            expr = re.compile("^oidc/(authenticate|callback)/$")
            if expr.match(path):
                logger.debug('** exclude path : authenticate')
                return None

            # Exclude every URL pointing to a list.
            # e.g: institution/  --> list of the institutions
            expr = re.compile("^[a-z0-9_]*/$")
            if expr.match(path):
                logger.debug('** exclude path : list template')
                return
        try:
            view_scopes = view_func.cls.keycloak_scopes
        except AttributeError:
            logger.debug('Allowing free acesss, since no authorization configuration (keycloak_scopes) found for this request route :%s', request) # noqa
            return None

        # Get default if method is not defined.
        required_scope = view_scopes.get(request.method, None) \
            if view_scopes.get(request.method, None) else view_scopes.get(
                'DEFAULT', None)

        # DEFAULT scope not found and DEFAULT_ACCESS is DENY
        if not required_scope and self.default_access == 'DENY':
            return JsonResponse(
                {"detail": unicode(PermissionDenied.default_detail)},
                status=PermissionDenied.status_code)

        try:
            # Get Token
            access_token = request.session['oidc_access_token']

            self.keycloak.load_authorization_config(
                "/srv/app/etc/keycloak/auth.json")
            # Get permissions
            permissions = self.keycloak.get_permissions(
                access_token,
                method_token_info='decode',
                key=import_from_settings('KEYCLOAK_RSA_PUBLIC_KEY'))
        except Exception:
            return JsonResponse(
                {"detail": unicode(AuthenticationFailed.default_detail)},
                status=AuthenticationFailed.status_code)
        for perm in permissions:
            if required_scope in perm.scopes:
                return None

        # User Permission Denied
        return JsonResponse(
            {"detail": unicode(PermissionDenied.default_detail)},
            status=PermissionDenied.status_code)

    def process_request(self, request):

        path = request.path_info.lstrip('/')

        # Exclude every URL pointing to the API service
        expr = re.compile("^api/.*$")
        if expr.match(path):
            logger.debug('** exclude path : API, not template')
            return

        # Home page
        if path == "":
            return

        # Exclude every URL pointing to a list.
        # e.g: institution/  --> list of the institutions
        expr = re.compile("^[a-z0-9_]*/$")
        if expr.match(path):
            logger.debug('** exclude path : list template')
            return

        # Exclude every URL pointing to a detail.
        # e.g: institution/1/  --> detail of an institution
        expr = re.compile("^[a-z0-9_]*/[0-9]*/$")
        if expr.match(path):
            logger.debug('** exclude path : detail template')
            return

        # Exclude every URL pointing to the API service,
        #   for authenticate
        expr = re.compile("^oidc/(authenticate|callback)/$")
        if expr.match(path):
            logger.debug('** exclude path : authenticate')
            return None

        if not request.user.is_authenticated():
            response = HttpResponseRedirect(
                reverse('oidc_authentication_init'))
            return response
