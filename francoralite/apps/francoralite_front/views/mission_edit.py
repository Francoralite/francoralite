# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..forms.mission import MissionForm
from ..francoralite_template_view import FrancoraliteFormView


class MissionEdit(FrancoraliteFormView):
    api_url_prefix = '/api/mission/'
    entity_name = 'mission'

    form_class = MissionForm
    template_name = '../templates/mission-add.html'
    template_variable_name = 'mission'

    success_url = '/mission/'

    keycloak_scopes = {
        'DEFAULT': 'mission:update',
    }

    def get_initial(self):
        initial = super().get_initial()
        initial['fonds'] = initial['fonds']['id']

        return initial
