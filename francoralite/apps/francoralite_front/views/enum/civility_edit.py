# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ...francoralite_template_view import FrancoraliteFormView
from ...forms.civility import CivilityForm


class CivilityEdit(FrancoraliteFormView):
    api_url_prefix = '/api/civility/'
    entity_name = 'civility'

    form_class = CivilityForm
    template_name = '../templates/enum/civility-add.html'
    template_variable_name = 'civility'

    success_url = '/civility/'

    keycloak_scopes = {
        'DEFAULT': 'civility:update',
    }
