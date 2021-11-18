# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from .. import tools
from ..forms.mission import MissionForm
from ..francoralite_template_view import FrancoraliteTemplateView


class MissionView(FrancoraliteTemplateView):
    template_name = '../templates/mission.html'
    keycloak_scopes = {
        'GET': 'mission:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(MissionView, self).get_context_data(**kwargs)
            context['missions'] = tools.request_api('/api/mission')
            context['form'] = MissionForm
        except Exception as err:
            context['missions'] = []
            context['error'] = err
        return context
