# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.usefulness import UsefulnessForm


class UsefulnessEdit(FrancoraliteFormView):
    template_name = "../templates/enum/usefulness-add.html"
    form_class = UsefulnessForm
    api_url_prefix = '/api/usefulness/'
    entity_name = 'usefulness'
    template_variable_name = 'usefulness'
    success_url = '/usefulness/'

    keycloak_scopes = {
        'DEFAULT': 'usefulness:update',
    }
