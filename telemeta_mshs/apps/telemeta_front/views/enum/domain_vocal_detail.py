# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from telemeta_front.forms.domain_vocal import DomainVocalForm
import telemeta_front.tools as tools


class DomainVocalDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_vocal-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainVocalDetail, self).get_context_data(**kwargs)
            context['domain_vocal'] = tools.request_api(
                '/api/domain_vocal/' + context['id'])
            context['form'] = DomainVocalForm()

        except Exception as err:
            context['domain_vocal'] = {}
            context['error'] = err.message
            context['form'] = DomainVocalForm()
        return context
