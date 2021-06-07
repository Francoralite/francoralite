# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools


class UsefulnessView(FrancoraliteTemplateView):
    template_name = "../templates/enum/usefulness.html"

    keycloak_scopes = {'GET': 'usefulness:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(UsefulnessView, self).get_context_data(**kwargs)
            context['usefulnesss'] = tools.request_api('/api/usefulness')
        except Exception as err:
            context['usefulnesss'] = []
            context['error'] = err.message

        return context
