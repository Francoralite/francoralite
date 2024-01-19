# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.musical_group import MusicalGroupForm


class MusicalGroupEdit(FrancoraliteFormView):
    template_name = "../templates/enum/musical_group-add.html"
    form_class = MusicalGroupForm
    api_url_prefix = '/api/musical_group/'
    entity_name = 'musical_group'
    template_variable_name = 'musical_group'
    success_url = '/musical_group/'

    keycloak_scopes = {
        'DEFAULT': 'musical_group:update',
    }
