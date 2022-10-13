# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ...francoralite_template_view import FrancoraliteFormView
from ...forms.block import BlockForm


class BlockEdit(FrancoraliteFormView):
    api_url_prefix = '/api/block/'
    entity_name = 'block'

    form_class = BlockForm
    template_name = '../templates/enum/block-add.html'
    template_variable_name = 'block'

    success_url = '/block/'

    keycloak_scopes = {
        'DEFAULT': 'block:update',
    }
