# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import requests

from settings import FRONT_HOST_URL, FRONT_HOST_URL_EXTERNAL
from telemeta_front.forms.item import ItemForm
from telemeta_front.forms.collection import CollectionForm
import telemeta_front.tools as tools


class ItemDetail(FrancoraliteTemplateView):
    template_name = "../templates/item-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(ItemDetail, self).get_context_data(**kwargs)
            context["url_external"] = FRONT_HOST_URL_EXTERNAL
            # Obtain values of the record item
            context["item"] = tools.request_api(
                '/api/item/' + context['id'] + '/complete')
            context['form'] = ItemForm()
            context['form_collection'] = CollectionForm()
            # Obtain values of related documents
            context['documents'] = tools.request_api(
                '/api/item/' + context['id'] + '/document')

            # Obtain gaphers of the record
            context['graphers'] = []
            context['graphers'].append(tools.request_api(
                 '/api/timeside/' + context['id'] + '/visualize'))

        except Exception as err:
            context['item'] = {}
            context['documents'] = []
            context['error'] = err.message
            response = requests.get(
                FRONT_HOST_URL+'/api/item/'+context['id'])

        return context
