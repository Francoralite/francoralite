# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ..francoralite_template_view import FrancoraliteTemplateView
import francoralite_front.tools as tools
from ..forms.item import ItemForm
from ..forms.collection import CollectionForm


class ItemDetail(FrancoraliteTemplateView):
    template_name = "../templates/item-detail.html"
    
    keycloak_scopes = {
        'DEFAULT': 'item:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(ItemDetail, self).get_context_data(**kwargs)
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
        except Http404:
            raise Http404(_('Cet item n’existe pas.'))
        except Exception as err:
            context['item'] = {}
            context['locations'] = []
            context['documents'] = []
            context['error'] = str(err) + ":" + str(type(err).__name__)
        return context
