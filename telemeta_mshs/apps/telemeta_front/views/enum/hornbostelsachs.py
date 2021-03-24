# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_mshs.apps.telemeta_front.tools as tools


class HornbostelsachsView(FrancoraliteTemplateView):
    template_name = "../templates/enum/hornbostelsachs.html"

    keycloak_scopes = {'GET': 'hornbostelsachs:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(HornbostelsachsView, self).get_context_data(
                **kwargs)
            context['hornbostelsachss'] = tools.request_api(
                '/api/hornbostelsachs')
        except Exception as err:
            context['hornbostelsachss'] = []
            context['error'] = err.message

        return context
