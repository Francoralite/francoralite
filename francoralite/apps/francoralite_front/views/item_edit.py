# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..forms.item import ItemForm
from ..francoralite_template_view import FrancoraliteFormView


class ItemEdit(FrancoraliteFormView):
    api_url_prefix = '/api/item/'
    entity_name = 'item'

    form_class = ItemForm
    template_name = '../templates/item-add.html'
    template_variable_name = 'item'

    success_url = '/item/'

    keycloak_scopes = {
        'DEFAULT': 'item:update',
    }