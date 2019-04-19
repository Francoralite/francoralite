# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class ThematicView(FrancoraliteTemplateView):
    template_name = "../templates/enum/thematic.html"

    keycloak_scopes = {'GET': 'thematic:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(ThematicView, self).get_context_data(**kwargs)
            context['thematics'] = tools.request_api('/api/thematic/')
        except Exception as err:
            context['thematics']
            context['error'] = err.message

        return context
