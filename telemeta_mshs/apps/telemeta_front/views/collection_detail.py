# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
from rest_framework import status
import requests

from settings import FRONT_HOST_URL
from telemeta_front.forms.collection import CollectionForm


class CollectionDetail(TemplateView):
    template_name = "../templates/collection-detail.html"

    def get_context_data(self, **kwargs):
        context = super(CollectionDetail, self).get_context_data(**kwargs)

        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL+'/api/collection/'+context['id'])
        if response.status_code == status.HTTP_200_OK:
            # Values of the collection
            context['collection'] = response.json
            context['form'] = CollectionForm()
            # Obtain values of the collectors (authority related table)

            # Collectors
            response_collectors = requests.get(
                FRONT_HOST_URL + '/api/collection/' + context['id']
                + '/collectors/')
            if response_collectors.status_code == status.HTTP_200_OK:
                # values of the Collectors
                context['collectors'] = response_collectors.json

            # Informers
            response_informers = requests.get(
                FRONT_HOST_URL + '/api/collection/' + context['id']
                + '/informer/')
            if response_informers.status_code == status.HTTP_200_OK:
                # values of the Informers
                context['informers'] = response_informers.json

            # Locations
            response_locations = requests.get(
                FRONT_HOST_URL + '/api/collection/' + context['id']
                + '/location/')
            if response_locations.status_code == status.HTTP_200_OK:
                # values of the Locations
                context['locations'] = response_locations.json

            # Languages
            response_languages = requests.get(
                FRONT_HOST_URL + '/api/collection/' + context['id']
                + '/language/')
            if response_languages.status_code == status.HTTP_200_OK:
                # values of the Laguages
                context['languages'] = response_languages.json

        return context
