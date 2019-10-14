# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
import requests
from rest_framework import status
from settings import FRONT_HOST_URL
from telemeta_front.forms.item import ItemForm
from rest_framework.parsers import MultiPartParser, FormParser
import telemeta_front.tools as tools


class ItemAdd(FormView):
    template_name = "../templates/item-add.html"
    form_class = ItemForm
    parser_classes = (MultiPartParser, FormParser)
    success_url = '/item/'

    def get_initial(self):
        initial = super(ItemAdd, self).get_initial()
        initial['collection'] = self.kwargs['id_collection']
        # Obtain code of the mission
        response = requests.get(
            FRONT_HOST_URL + '/api/collection/' + self.kwargs['id_collection'])
        if response.status_code == status.HTTP_200_OK:
            initial['code'] = response.json()['code']
        return initial

    def post(self, request, *args, **kwargs):
        return tools.post(
            'item', ItemForm, request, *args, **kwargs)
