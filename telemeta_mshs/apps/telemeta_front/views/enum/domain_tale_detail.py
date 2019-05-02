# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from telemeta_front.forms.domain_tale import DomainTaleForm
import telemeta_front.tools as tools


class DomainTaleDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_tale-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainTaleDetail, self).get_context_data(**kwargs)
            context['domain_tale'] = tools.request_api(
                '/api/domain_tale/' + context['id'])
            context['form'] = DomainTaleForm()

        except Exception as err:
            context['domain_tale'] = {}
            context['error'] = err.message
            context['form'] = DomainTaleForm()
        return context
