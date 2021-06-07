# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.forms.hornbostelsachs import HornbostelsachsForm
import francoralite.apps.francoralite_front.tools as tools


class HornbostelsachsDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/hornbostelsachs-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(HornbostelsachsDetail, self).get_context_data(
                **kwargs)
            context['hornbostelsachs'] = tools.request_api(
                '/api/hornbostelsachs/' + context['id'])
            context['form'] = HornbostelsachsForm()

        except Exception as err:
            context['hornbostelsachs'] = {}
            context['error'] = err.message
            context['form'] = HornbostelsachsForm()
        return context
