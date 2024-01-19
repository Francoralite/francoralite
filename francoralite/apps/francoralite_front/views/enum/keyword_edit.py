# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.keyword import KeywordForm


class KeywordEdit(FrancoraliteFormView):
    template_name = "../templates/enum/keyword-add.html"
    form_class = KeywordForm
    api_url_prefix = '/api/keyword/'
    entity_name = 'keyword'
    template_variable_name = 'keyword'
    success_url = '/keyword/'

    keycloak_scopes = {
        'DEFAULT': 'keyword:update',
    }
