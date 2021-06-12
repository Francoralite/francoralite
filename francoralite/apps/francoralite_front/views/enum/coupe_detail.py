# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.forms.coupe import CoupeForm
import francoralite.apps.francoralite_front.tools as tools


class CoupeDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/coupe-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(CoupeDetail, self).get_context_data(**kwargs)
            context['coupe'] = tools.request_api(
                '/api/coupe/' + context['id'])
            context['form'] = CoupeForm()

        except Exception as err:
            context['coupe'] = {}
            context['error'] = err.message
            context['form'] = CoupeForm()
        return context
