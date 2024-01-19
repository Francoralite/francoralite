# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..forms.institution import InstitutionForm
from ..francoralite_template_view import FrancoraliteFormView


class InstitutionEdit(FrancoraliteFormView):
    api_url_prefix = '/api/institution/'
    entity_name = 'institution'

    form_class = InstitutionForm
    template_name = '../templates/institution-add.html'
    template_variable_name = 'institution'

    success_url = '/institution/'

    keycloak_scopes = {
        'DEFAULT': 'institution:update',
    }
