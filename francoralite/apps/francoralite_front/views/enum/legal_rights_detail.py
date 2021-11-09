# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.forms.legal_rights import LegalRightsForm
import francoralite.apps.francoralite_front.tools as tools


class LegalRightsDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/legal_rights-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(LegalRightsDetail, self).get_context_data(**kwargs)
            context['legal_rights'] = tools.request_api(
                '/api/legalrights/' + context['id'])
            context['form'] = LegalRightsForm()

        except Exception as err:
            context['legal_rights'] = {}
            context['error'] = err
            context['form'] = LegalRightsForm()
        return context
