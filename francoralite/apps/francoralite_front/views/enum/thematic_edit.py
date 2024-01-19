# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.thematic import ThematicForm


class ThematicEdit(FrancoraliteFormView):
    template_name = "../templates/enum/thematic-add.html"
    form_class = ThematicForm
    api_url_prefix = '/api/thematic/'
    entity_name = 'thematic'
    template_variable_name = 'thematic'
    success_url = '/thematic/'

    keycloak_scopes = {
        'DEFAULT': 'thematic:update',
    }
