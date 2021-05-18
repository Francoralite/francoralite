# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import requests
from django.conf import settings
from telemeta_mshs.apps.telemeta_front.forms.item import ItemForm


class ItemView(FrancoraliteTemplateView):
    template_name = "../templates/item.html"

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['items'] = requests.get(
            settings.FRONT_HOST_URL + '/api/item').json
        context['form'] = ItemForm
        return context
