# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools


class CulturalAreaView(FrancoraliteTemplateView):
    template_name = "../templates/enum/cultural_area.html"

    keycloak_scopes = {'GET': 'cultural_area:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(CulturalAreaView, self).get_context_data(**kwargs)
            context['cultural_areas'] = tools.request_api('/api/cultural_area')
        except Exception as err:
            context['cultural_areas'] = []
            context['error'] = err

        return context
