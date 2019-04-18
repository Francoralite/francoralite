# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class FondView(FrancoraliteTemplateView):
    template_name = "../templates/fond.html"
    keycloak_scopes = {
        'GET': 'fond:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(FondView, self).get_context_data(**kwargs)
            context['fonds'] = tools.request_api('/api/fond')
        except Exception as err:
            context['fonds'] = []
            context['error'] = err.message
        return context
