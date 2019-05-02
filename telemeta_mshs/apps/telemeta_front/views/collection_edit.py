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
from .related import query_related, write_relations
import telemeta_front.tools as tools


class CollectionEdit(FormView):
    template_name = "../templates/collection-add.html"
    form_class = CollectionForm
    success_url = '/collection/'
    keycloak_scopes = {
            'GET': 'collection:view',
            'POST': 'collection:add',
            'PATCH': 'collection:update',
            'PUT': 'collection:update'}

    def get_context_data(self, **kwargs):
        try:
            context = super(CollectionEdit, self).get_context_data(**kwargs)
            id = kwargs.get('id')
            # Obtain values of the record
            context['collection'] = tools.request_api(
                '/api/collection/' + str(id))
        except Exception as err:
            context['collection'] = {}
            context['error'] = err.message
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
                    write_relations(id,
                                    "collection",
                                    collectors,
                                    url_collectors,
                                    "collector")

                    # Informers
                    informers = json.loads(request.POST['informers'])
                    url_informers = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/informer/'
                    write_relations(id,
                                    "collection",
                                    informers,
                                    url_informers,
                                    "informer")
                    # Locations
                    locations = json.loads(request.POST['locations'])
                    url_locations = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/location/'
                    write_relations(id,
                                    "collection",
                                    locations,
                                    url_locations,
                                    "location")

                    # Languages
                    languages = json.loads(request.POST['languages'])
                    url_languages = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/language/'
                    write_relations(id,
                                    "collection",
                                    languages,
                                    url_languages,
                                    "language")

                    # Publishers
                    publishers = json.loads(request.POST['publishers'])
                    url_publishers = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/publisher/'
                    write_relations(id,
                                    "collection",
                                    publishers,
                                    url_publishers,
                                    "publisher")

                    # Performances
                    performances_selected = json.loads(
                        request.POST['performances'])
                    url_performances = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/performance/'
                    write_relations(id,
                                    "collection",
                                    performances_selected,
                                    url_performances,
                                    "")
                    index = 0
                    # Request the performances ordered by ID
                    performances = query_related(
                        url_performances + "?ordering=id")

                    for performance in performances_selected:
                        if "id" not in performance:
                            # The performance wasn't exist.
                            # Search and retrieve the ID of the new performance
                            # in the database
                            performance["id"] = performances[index]["id"]

                        if("informers" in performance):
                            url_musicians = \
                                FRONT_HOST_URL + '/api/collection/' + \
                                str(collection["id"]) + '/performance/' + \
                                str(performance["id"]) + '/musician/'
                            write_relations(performance["id"],
                                            "performance_collection",
                                            performance["informers"],
                                            url_musicians,
                                            "musician")
                        index = index + 1

                return HttpResponseRedirect('/collection/')

            except RequestException:
                return HttpResponseRedirect('/collection/edit')

        return HttpResponseRedirect('/collection/edit')
