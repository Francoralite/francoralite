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
import json
from related import write_relations, query_related


class CollectionAdd(FormView):
    template_name = "../templates/collection-add.html"
    form_class = CollectionForm
    success_url = '/collection/'

    def get_initial(self):
        initial = super(CollectionAdd, self).get_initial()
        initial['mission'] = self.kwargs['id_mission']
        # Obtain code of the mission
        response = requests.get(
            FRONT_HOST_URL + '/api/mission/' + self.kwargs['id_mission'])
        if response.status_code == status.HTTP_200_OK:
            initial['code'] = response.json()['code']
        return initial

    def post(self, request, *args, **kwargs):
        id_institution = kwargs['id_institution']
        id_fond = kwargs['id_fond']
        id_mission = kwargs['id_mission']

        form = CollectionForm(request.POST)

        if form.is_valid():

            try:
                response = requests.post(
                    FRONT_HOST_URL + '/api/collection/',
                    data=form.cleaned_data
                )
                if response.status_code == status.HTTP_201_CREATED:
                    collection = response.json()

                    # Collectors
                    collectors = json.loads(request.POST['collectors'])
                    url_collectors = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/collectors/'
                    # Create collectors
                    write_relations(collection["id"],
                                    "collection", collectors,
                                    url_collectors, "collector")

                    # Informers
                    informers = json.loads(request.POST['informers'])
                    url_informers = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/informer/'
                    # Create informers
                    write_relations(collection["id"],
                                    "collection", informers,
                                    url_informers, "informer")

                    # Locations
                    locations = json.loads(request.POST['locations'])
                    url_locations = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/location/'
                    # Create locations
                    write_relations(collection["id"],
                                    "collection", locations,
                                    url_locations, "location")

                    # Languages
                    languages = json.loads(request.POST['languages'])
                    url_languages = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/language/'
                    # Create languages
                    write_relations(collection["id"],
                                    "collection", languages,
                                    url_languages, "language")

                    # Publishers
                    publishers = json.loads(request.POST['publishers'])
                    url_publishers = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/publisher/'
                    # Create publishers
                    write_relations(collection["id"],
                                    "collection", publishers,
                                    url_publishers, "publisher")

                    # Performances
                    performances_selected = json.loads(
                        request.POST['performances'])
                    url_performances = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/performance/'
                    # Create performances
                    write_relations(collection["id"],
                                    "collection", performances_selected,
                                    url_performances, "")
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
                return HttpResponseRedirect(
                    '/institution/' + id_institution + '/fond/'
                    + id_fond + '/mission/' + id_mission + '/collection/add')

        return HttpResponseRedirect(
            '/institution/' + id_institution + '/fond/'
            + id_fond + '/mission/' + id_mission + '/collection/add')
