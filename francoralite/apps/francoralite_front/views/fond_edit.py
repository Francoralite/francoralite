# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ..forms.fond import FondForm
from ..francoralite_template_view import FrancoraliteFormView


class FondEdit(FrancoraliteFormView):
    api_url_prefix = '/api/fond/'
    entity_name = 'fond'
    
    template_name = "../templates/fond-add.html"
    form_class = FondForm
    template_variable_name = 'fond'
    success_url = '/fond/'
    keycloak_scopes = {
        'DEFAULT': 'fond:update',
    }
