# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import status
from settings import FRONT_HOST_URL
import requests

from django.http import HttpResponseRedirect
from requests.exceptions import RequestException

from telemeta_front.errors import APPLICATION_ERRORS

HTTP_ERRORS = {
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
    hed = {'Authorization': 'Bearer ' + auth_token}
    return hed


def request_api(endpoint):
    """
    TODO: A renseigner
    """

    try:
        response = requests.get(
            FRONT_HOST_URL + endpoint)

        if response.status_code == status.HTTP_200_OK:
            return response.json

        raise Exception(HTTP_ERRORS[response.status_code])
    except Exception:
        raise


def post(entity, form_entity, request, *args, **kwargs):

    form = form_entity(request.POST)

    entity_api = entity
    if entity in PROBLEM_NAMES:
        entity_api = entity.replace('_', '')

    if form.is_valid():
        try:
            post_api(FRONT_HOST_URL + '/api/' + entity_api + '/',
                     data=form.cleaned_data,
                     request=request)
            return HttpResponseRedirect('/' + entity + '/')

        except RequestException:
            return HttpResponseRedirect('/' + entity + '/add')

    return HttpResponseRedirect('/' + entity + '/add')


def post_api(endpoint, data, request):
    """
    TODO: A renseigner
    """

    try:
        response = requests.post(
            endpoint, data=data,
            headers=get_token_header(request=request))

        if response.status_code == status.HTTP_201_CREATED or \
                response.status_code == status.HTTP_200_OK:
            return response.json

        raise Exception(HTTP_ERRORS[response.status_code])
    except Exception:
        raise


def patch(entity, form_entity, request, *args, **kwargs):
    form = form_entity(request.POST)
    id = kwargs.get('id')

    entity_api = entity
    if entity in PROBLEM_NAMES:
        entity_api = entity.replace('_', '')

    if form.is_valid():
        try:
            response = patch_api(
                FRONT_HOST_URL + '/api/' + entity_api + '/' + str(id) + '/',
                data=form.cleaned_data,
                request=request
            )
            if(response.status_code != status.HTTP_200_OK):
                return HttpResponseRedirect('/' + entity + '/edit/' +
                                            str(id))
            return HttpResponseRedirect('/' + entity + '/')

        except RequestException:
            return HttpResponseRedirect('/' + entity + '/edit')

    return HttpResponseRedirect('/' + entity + '/edit')


def patch_api(endpoint, data, request):

    try:
        response = requests.patch(
            endpoint,
            data=data,
            headers=get_token_header(request=request)
        )
        if response.status_code == status.HTTP_200_OK:
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
            FRONT_HOST_URL + '/api/' + entity_api + '/' + str(id),
            request=request
            )
        return HttpResponseRedirect('/' + entity + '/')

    except RequestException:
        return HttpResponseRedirect('/' + entity + '/')


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
