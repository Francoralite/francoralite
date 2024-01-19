# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from francoralite.apps.francoralite_front.forms.dance import DanceForm


class DanceEdit(FrancoraliteFormView):
    api_url_prefix = '/api/dance/'
    entity_name = 'dance'
    
    form_class = DanceForm
    template_name = "../templates/enum/dance-add.html"
    template_variable_name = 'dance'
        
    success_url = '/dance/'
    
    keycloak_scopes = {
        'DEFAULT': 'dance:update',
    }
