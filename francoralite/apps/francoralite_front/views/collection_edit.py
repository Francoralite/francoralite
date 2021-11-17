# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..forms.collection import CollectionForm
from ..francoralite_template_view import FrancoraliteFormView


class CollectionEdit(FrancoraliteFormView):
    api_url_prefix = '/api/collection/'
    entity_name = 'collection'

    form_class = CollectionForm
    template_name = '../templates/collection-add.html'
    template_variable_name = 'collection'

    success_url = '/collection/'

    keycloak_scopes = {
        'DEFAULT': 'collection:update',
    }
