# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from rest_framework import status
import requests

from settings import FRONT_HOST_URL
from telemeta_front.forms.item import ItemForm


class ItemDetail(FrancoraliteTemplateView):
    template_name = "../templates/item-detail.html"

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)

        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL+'/api/item/'+context['id'])
        if response.status_code == status.HTTP_200_OK:
            context['item'] = response.json
            context['form'] = ItemForm()

        # Obtain gaphers of the record
        context['graphers'] = []
        response = requests.get(
            FRONT_HOST_URL+'/api/timeside/' + context['id'] + '/visualize/')
        if response.status_code == status.HTTP_200_OK:
            context['graphers'].append(response.json)

        return context
