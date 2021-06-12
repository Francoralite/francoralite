# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools


class LegalRightsView(FrancoraliteTemplateView):
    template_name = "../templates/enum/legal_rights.html"

    keycloak_scopes = {'GET': 'legal_rights:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(LegalRightsView, self).get_context_data(**kwargs)
            context['legal_rights'] = tools.request_api('/api/legalrights')
        except Exception as err:
            context['legal_rights'] = []
            context['error'] = err.message

        return context
