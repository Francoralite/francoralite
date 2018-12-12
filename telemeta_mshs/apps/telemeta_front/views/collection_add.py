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
from related import create_related_records


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
                    create_related_records(
                        collectors, url_collectors,
                        "collector", "collection", collection["id"])

                    # Informers
                    informers = json.loads(request.POST['informers'])
                    url_informers = \
                        FRONT_HOST_URL + '/api/collection/' + \
                        str(collection["id"]) + '/informer/'

                    # Create informers
                    create_related_records(
                        informers, url_informers,
                        "informer", "collection", collection["id"])

                return HttpResponseRedirect('/collection/')

            except RequestException:
                return HttpResponseRedirect(
                    '/institution/' + id_institution + '/fond/'
                    + id_fond + '/mission/' + id_mission + '/collection/add')

        return HttpResponseRedirect(
            '/institution/' + id_institution + '/fond/'
            + id_fond + '/mission/' + id_mission + '/collection/add')
