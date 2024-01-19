# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import requests

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.utils.translation import gettext as _
from requests.exceptions import RequestException
from rest_framework import status

from francoralite.apps.francoralite_front.errors import APPLICATION_ERRORS
from .views.related import (
    write_fond_related,
    write_mission_related,
    write_collection_related,
    write_item_related)


HTTP_ERRORS = {
    status.HTTP_400_BAD_REQUEST: APPLICATION_ERRORS['HTTP_API_400'],
    status.HTTP_401_UNAUTHORIZED: APPLICATION_ERRORS['HTTP_API_401'],
    status.HTTP_403_FORBIDDEN: APPLICATION_ERRORS['HTTP_API_403'],
    status.HTTP_404_NOT_FOUND: APPLICATION_ERRORS['HTTP_API_404'],
    status.HTTP_409_CONFLICT: APPLICATION_ERRORS['HTTP_API_409'],
}


PROBLEM_NAMES = [
    "legal_rights",
    "recording_context",
    "location_gis",
]


class UserMessageError(RequestException): pass


def get_token_header(request):
    """
    TODO: À renseigner
    """

    auth_token = request.session.get('oidc_access_token')
    if auth_token:
        return {'Authorization': 'Bearer ' + auth_token}
    else:
        return {}


def check_status_code(status_code, allowed_codes=(status.HTTP_200_OK,)):
    """
    TODO: À renseigner
    """

    if status_code == status.HTTP_403_FORBIDDEN:
        raise PermissionDenied(_('Accès interdit.'))

    if status_code == status.HTTP_404_NOT_FOUND:
        raise Http404(_('Cette fiche n’existe pas.'))

    if status_code == status.HTTP_409_CONFLICT:
        raise UserMessageError(_('Une fiche avec ce code existe déjà.'))

    if status.HTTP_400_BAD_REQUEST <= status_code < status.HTTP_500_INTERNAL_SERVER_ERROR:
        raise RequestException()

    if status_code not in allowed_codes:
        raise Exception(HTTP_ERRORS[status_code])


def handle_message_from_exception(request, exception):
    """
    TODO: À renseigner
    """

    if isinstance(exception, UserMessageError):
        messages.add_message(request, messages.ERROR, exception)

    elif exception is not None:
        messages.add_message(request, messages.ERROR,
                             _('Une erreur indéterminée est survenue.'))


def request_api(endpoint):
    """
    TODO: À renseigner
    """

    response = requests.get(settings.FRONT_HOST_URL + endpoint)

    check_status_code(response.status_code)

    return response.json()


def post(entity, form_entity, request, *args, **kwargs):
    """
    TODO: À renseigner
    """

    form = form_entity(request.POST, request.FILES)
    entity_api = entity
    entity_url = entity

    # Processing the problem names entities
    if entity in PROBLEM_NAMES:
        entity_api = entity.replace('_', '')

    # Processing URL for Mission entity
    if entity == 'fond':
        entity_url = 'institution/' + kwargs['id_institution'] \
            + '/' + entity
    # Processing URL for Mission entity
    if entity == 'mission':
        entity_url = 'institution/' + kwargs['id_institution'] \
            + '/fond/' + kwargs['id_fond']\
            + '/' + entity
    # Processing URL for Collection entity
    if entity == 'collection':
        entity_url = 'institution/' + kwargs['id_institution'] \
            + '/fond/' + kwargs['id_fond']\
            + '/mission/' + kwargs['id_mission'] \
            + '/' + entity
    # Processing URL for Item entity
    if entity == 'item':
        entity_url = 'institution/' + kwargs['id_institution'] \
            + '/fond/' + kwargs['id_fond']\
            + '/mission/' + kwargs['id_mission'] \
            + '/collection/' + kwargs['id_collection'] \
            + '/' + entity

    # Problem with old Telemeta fields/entities
    if form.is_valid():
        if entity == 'item':
            # Concatenate domains
            form.cleaned_data['domain'] = ''.join(form.cleaned_data['domain'])
            # Remove the 'file' entry : if not, there some bugs
            del form.cleaned_data['file']
        try:
            entity_json = post_api(
                settings.FRONT_HOST_URL + '/api/' + entity_api,
                data=form.cleaned_data,
                request=request,
                entity=entity,
            )

            messages.add_message(request, messages.SUCCESS,
                                 _('La fiche a bien été créée.'))

            if entity == 'fond':
                return HttpResponseRedirect(
                    '/institution/' +
                    str(form.cleaned_data['institution']))

            if entity == 'item':
                return HttpResponseRedirect(
                    '/item/' +
                    str(entity_json['id']))

            # Previous page ( not an add page ... )
            if len(request.session.get("referers", [])) > 1:
                for referer in request.session["referers"]:
                    if 'add' not in referer.split('/'):
                        return HttpResponseRedirect(referer)
            return HttpResponseRedirect('/' + entity)

        except RequestException as e:
            handle_message_from_exception(request, e)

    else:
        for errors in form.errors.values():
            for error in errors:
                messages.add_message(request, messages.ERROR, error)

    return HttpResponseRedirect('/' + entity_url + '/add')


def post_api(endpoint, data, request, entity):
    """
    TODO: À renseigner
    """

    headers = get_token_header(request=request)
    response = requests.post(
        endpoint,
        data=data,
        files=request.FILES,
        headers=headers,
    )

    check_status_code(response.status_code,
                      allowed_codes=(status.HTTP_200_OK,
                                     status.HTTP_201_CREATED))

    entity_json = response.json()
    if entity == "fond":
        write_fond_related(entity_json, request, headers)
    if entity == "mission":
        write_mission_related(entity_json, request, headers)
    if entity == "collection":
        write_collection_related(entity_json, request, headers)
    if entity == "item":
        write_item_related(entity_json, request, headers)
    return entity_json


def patch(entity, form_entity, request, *args, **kwargs):
    """
    TODO: À renseigner
    """

    form = form_entity(request.POST)
    form.current_id = id = int(kwargs.get('id'))
    if entity == 'item':
        form.fields['file'].required = False

    entity_api = entity
    if entity in PROBLEM_NAMES:
        entity_api = entity.replace('_', '')

    if form.is_valid():
        if entity == "collection":
            form.cleaned_data['recorded_from_year'] = \
                form.data['recorded_from_year']
            form.cleaned_data['recorded_to_year'] = \
                form.data['recorded_to_year']
            if form.cleaned_data['year_published'] is None:
                form.cleaned_data['year_published'] = ''
        if entity == "item":
            # Concatenate domains
            form.cleaned_data['domain'] = ''.join(form.cleaned_data['domain'])
        try:
            patch_api(
                settings.FRONT_HOST_URL + '/api/' + entity_api + '/' + str(id),
                data=form.cleaned_data,
                request=request,
                entity=entity
            )

            messages.add_message(request, messages.SUCCESS,
                                 _('La fiche a bien été mise à jour.'))

            # Previous page ( not an edit page ... )
            if len(request.session.get("referers", [])) > 1:
                for referer in request.session["referers"]:
                    if 'edit' not in referer.split('/'):
                        return HttpResponseRedirect(referer)
            return HttpResponseRedirect('/' + entity)

        except RequestException as e:
            handle_message_from_exception(request, e)

    else:
        for errors in form.errors.values():
            for error in errors:
                messages.add_message(request, messages.ERROR, error)

    return HttpResponseRedirect('/' + entity + '/edit/' + str(id))


def patch_api(endpoint, data, request, entity):
    """
    TODO: À renseigner
    """

    response = requests.patch(
        endpoint,
        data=data,
        headers=get_token_header(request=request),
    )

    check_status_code(response.status_code)

    entity_json = response.json()
    if entity == "fond":
        write_fond_related(
            entity_json,
            request,
            headers=get_token_header(request=request),
        )
    if entity == "mission":
        write_mission_related(
            entity_json,
            request,
            headers=get_token_header(request=request),
        )
    if entity == "collection":
        write_collection_related(
            entity_json,
            request,
            headers=get_token_header(request=request),
        )
    if entity == "item":
        write_item_related(
            entity_json,
            request,
            headers=get_token_header(request=request),
        )

    return response


def delete(entity, request, *args, **kwargs):
    """
    TODO: À renseigner
    """

    id = kwargs.get('id')
    entity_api = entity

    if entity in PROBLEM_NAMES:
        entity_api = entity.replace('_', '')
    try:
        delete_api(
            settings.FRONT_HOST_URL + '/api/' + entity_api + '/' + str(id),
            request=request,
        )

        messages.add_message(request, messages.SUCCESS,
                             _('La fiche a bien été supprimée.'))

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except RequestException as e:
        handle_message_from_exception(request, e)
        return HttpResponseRedirect('/' + entity)


def delete_api(endpoint, request):
    """
    TODO: À renseigner
    """

    response = requests.delete(
        endpoint,
        headers=get_token_header(request=request),
    )

    check_status_code(response.status_code,
                      allowed_codes=(status.HTTP_200_OK,
                                     status.HTTP_204_NO_CONTENT))

    return response
