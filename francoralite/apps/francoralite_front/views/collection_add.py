# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.collection import CollectionForm
import francoralite.apps.francoralite_front.tools as tools


class CollectionAdd(FormView):
    template_name = "../templates/collection-add.html"
    form_class = CollectionForm
    success_url = '/collection/'

    def get_initial(self):
        initial = super(CollectionAdd, self).get_initial()
        initial['mission'] = self.kwargs['id_mission']
        # Obtain code of the mission
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/mission/' + self.kwargs['id_mission'])
         # Obtain code the collection
        if response.status_code == status.HTTP_200_OK:
            response_c = requests.get(
                settings.FRONT_HOST_URL + '/api/collection?mission=' + self.kwargs['id_mission'] + '&ordering=code')
            data_c = response_c.json()
            if len(data_c) > 0:
                # Retrieve last code
                last_code = data_c[-1]['code']
                # Compose new code
                n = 4
                initial['code'] = last_code[:-n] + str( int( last_code[-n:] ) + 1 ).zfill(n)
            else:
                initial['code'] = response.json()['code'] + "_0001"
     
        return initial

    def post(self, request, *args, **kwargs):
        return tools.post(
            'collection', CollectionForm, request, *args, **kwargs)
