# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.forms.coirault import CoiraultForm
import francoralite.apps.francoralite_front.tools as tools


class CoiraultDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/coirault-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(CoiraultDetail, self).get_context_data(**kwargs)
            context['coirault'] = tools.request_api(
                '/api/skos_concept/' + context['id'])
            context['form'] = CoiraultForm()

        except Exception as err:
            context['coirault'] = {}
            context['error'] = err
            context['form'] = CoiraultForm()
        return context
