# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.language import LanguageForm


class LanguageEdit(FrancoraliteFormView):
    template_name = "../templates/enum/language-add.html"
    api_url_prefix = '/api/language/'
    entity_name = 'language'
    form_class = LanguageForm
    template_variable_name = 'language'
    success_url = '/language/'

    keycloak_scopes = {
            'GET': 'language:view',
            'POST': 'language:add',
            'PATCH': 'language:update',
            'PUT': 'language:update'}
