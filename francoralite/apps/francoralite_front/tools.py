# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import status
from django.conf import settings
import requests

from django.http import HttpResponseRedirect, Http404
from requests.exceptions import RequestException

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
}

PROBLEM_NAMES = [
    "legal_rights",
    "recording_context",
    "location_gis"
    ]


def get_token_header(request):
    auth_token = request.session['oidc_access_token']
    head = {'Authorization': 'Bearer ' + auth_token}
    return head


def request_api(endpoint):
    """
    TODO: A renseigner
    """

    try:
        response = requests.get(
            settings.FRONT_HOST_URL + endpoint)

        if response.status_code == status.HTTP_200_OK:
            return response.json()

        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise Http404()
        
        raise Exception(HTTP_ERRORS[response.status_code])
    except Exception:
        raise


def post(entity, form_entity, request, *args, **kwargs):

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
            post_api(settings.FRONT_HOST_URL + '/api/' + entity_api,
                     data=form.cleaned_data,
                     request=request,
                     entity=entity)
            if entity == 'fond':
                return HttpResponseRedirect(
                    '/institution/' +
                    str(form.cleaned_data['institution']))
            # Previous page ( not an edit page ... )
            if len(request.session["referers"]) > 1:
                try:
                    for referer in request.session["referers"]:
                        if 'add' not in referer.split('/'):
                            return HttpResponseRedirect(referer)
                except Exception:
                    return HttpResponseRedirect('/' + entity)
            return HttpResponseRedirect('/' + entity)

        except RequestException:
            return HttpResponseRedirect('/' + entity_url + '/add')

    return HttpResponseRedirect('/' + entity_url + '/add')


def post_api(endpoint, data, request, entity):
    """
    TODO: A renseigner
    """

    try:
        headers = get_token_header(request=request)
        response = requests.post(
            endpoint,
            data=data,
            files=request.FILES,
            headers=headers)
        if response.status_code == status.HTTP_201_CREATED or \
                response.status_code == status.HTTP_200_OK:
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

        raise Exception(HTTP_ERRORS[response.status_code])
    except Exception:
        raise


def patch(entity, form_entity, request, *args, **kwargs):
    form = form_entity(request.POST)
    if entity == 'item':
        form.fields['file'].required = False
    id = kwargs.get('id')

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
            response = patch_api(
                settings.FRONT_HOST_URL + '/api/' + entity_api + '/' + str(id),
                data=form.cleaned_data,
                request=request,
                entity=entity
            )
            if(response.status_code != status.HTTP_200_OK):
                return HttpResponseRedirect('/' + entity + '/edit/' +
                                            str(id))
            # Previous page ( not an edit page ... )
            if len(request.session["referers"]) > 1:
                for referer in request.session["referers"]:
                    if 'edit' not in referer.split('/'):
                        return HttpResponseRedirect(referer)
            return HttpResponseRedirect('/' + entity)

        except RequestException:
            return HttpResponseRedirect('/' + entity + '/edit/' + str(id))

    return HttpResponseRedirect('/' + entity + '/edit/' + str(id))


def patch_api(endpoint, data, request, entity):
    try:
        response = requests.patch(
            endpoint,
            data=data,
            headers=get_token_header(request=request)
        )
        if response.status_code == status.HTTP_200_OK:
            entity_json = response.json()
            if entity == "fond":
                write_fond_related(
                    entity_json,
                    request,
                    headers=get_token_header(request=request))
            if entity == "mission":
                write_mission_related(
                    entity_json,
                    request,
                    headers=get_token_header(request=request))
            if entity == "collection":
                write_collection_related(
                    entity_json,
                    request,
                    headers=get_token_header(request=request))
            if entity == "item":
                write_item_related(
                    entity_json,
                    request,
                    headers=get_token_header(request=request))
        return response

    except Exception:
        raise


def delete(entity, request, *args, **kwargs):
    id = kwargs.get('id')
    entity_api = entity

    if entity in PROBLEM_NAMES:
        entity_api = entity.replace('_', '')
    try:
        delete_api(
            settings.FRONT_HOST_URL + '/api/' + entity_api + '/' + str(id),
            request=request
            )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except RequestException:
        return HttpResponseRedirect('/' + entity)


def delete_api(endpoint, request):
    """
    TODO: A renseigner
    """
    try:
        requests.delete(
            endpoint,
            headers=get_token_header(request=request)
            )
    except Exception:
        raise
