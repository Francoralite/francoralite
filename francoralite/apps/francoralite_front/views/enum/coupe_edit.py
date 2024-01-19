# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ...francoralite_template_view import FrancoraliteFormView
from ...forms.coupe import CoupeForm


class CoupeEdit(FrancoraliteFormView):
    api_url_prefix = '/api/coupe/'
    entity_name = 'coupe'

    form_class = CoupeForm
    template_name = '../templates/enum/coupe-add.html'
    template_variable_name = 'coupe'

    success_url = '/coupe/'

    keycloak_scopes = {
        'DEFAULT': 'coupe:update',
    }
