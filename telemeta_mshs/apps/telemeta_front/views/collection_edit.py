# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from rest_framework import status
import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.collection import CollectionForm
from django.shortcuts import render
import json
from .collection_related import compare_related


class CollectionEdit(FormView):
    template_name = "../templates/collection-add.html"
    form_class = CollectionForm
    success_url = '/collection/'

    def get_context_data(self, **kwargs):
        context = super(CollectionEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/extcollection/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['collection'] = response.json

        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        collection = requests.get(
            FRONT_HOST_URL + '/api/collection/' + str(id))
        data = collection.json()
        data['mission'] = data['mission']['id']

        form = CollectionForm(initial=data)

        return render(request,
                      '../templates/collection-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = CollectionForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/collection/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):

                    return HttpResponseRedirect(
                        '/collection/edit/' + str(id))
                else:
                    collection = response.json()

                    # Collectors
                    collectors = json.loads(request.POST['collectors'])
                    url_collectors = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/collectors/'
                    compare_related(
                        collectors, url_collectors, "collector", id)

                    # Informers
                    informers = json.loads(request.POST['informers'])
                    url_informers = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/informer/'
                    compare_related(
                        informers, url_informers, "informer", id)

                    # Locations
                    locations = json.loads(request.POST['locations'])
                    url_locations = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/location/'
                    compare_related(
                        locations, url_locations, "location", id)

                    # Languages
                    languages = json.loads(request.POST['languages'])
                    url_languages = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/language/'
                    compare_related(
                        languages, url_languages, "language", id)

                return HttpResponseRedirect('/collection/')

            except RequestException:
                return HttpResponseRedirect('/collection/edit')

        return HttpResponseRedirect('/collection/edit')
