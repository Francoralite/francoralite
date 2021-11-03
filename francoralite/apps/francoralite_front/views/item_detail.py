# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import requests

from django.conf import settings
from francoralite.apps.francoralite_front.forms.item import ItemForm
from francoralite.apps.francoralite_front.forms.collection import CollectionForm
import francoralite.apps.francoralite_front.tools as tools


class ItemDetail(FrancoraliteTemplateView):
    template_name = "../templates/item-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(ItemDetail, self).get_context_data(**kwargs)
            context["url_external"] = settings.FRONT_HOST_URL_EXTERNAL
            # Obtain values of the record item
            context["item"] = tools.request_api(
                '/api/item/' + context['id'] + '/complete')
            context['form'] = ItemForm()
            context['form_collection'] = CollectionForm()
            # Obtain values of related documents
            context['documents'] = tools.request_api(
                '/api/item/' + context['id'] + '/document')
            locations = tools.request_api(
                '/api/collection/'
                + str(context["item"]["collection"]["id"])
                + '/location')
            context['locations'] = []
            for l in locations:
                context['locations'].append(l["location"])
            #   - performances
            performances = tools.request_api(
                '/api/item/'
                + context['id']
                + '/performance')
            context['performances'] = performances

        except Exception as err:
            context['item'] = {}
            context['locations'] = []
            context['documents'] = []
            context['error'] = err
            response = requests.get(
                settings.FRONT_HOST_URL + '/api/item/' + context['id'])

        return context
