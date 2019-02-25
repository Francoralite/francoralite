# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
import requests
from settings import FRONT_HOST_URL
from telemeta_front.forms.item import ItemForm


class ItemView(TemplateView):
    template_name = "../templates/item.html"

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['items'] = requests.get(
            FRONT_HOST_URL + '/api/item/').json
        context['form'] = ItemForm
        return context
