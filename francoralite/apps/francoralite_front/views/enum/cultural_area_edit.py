# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ...francoralite_template_view import FrancoraliteFormView
from ...forms.cultural_area import CulturalAreaForm


class CulturalAreaEdit(FrancoraliteFormView):
    api_url_prefix = '/api/cultural_area/'
    entity_name = 'cultural_area'

    form_class = CulturalAreaForm
    template_name = '../templates/enum/cultural_area-add.html'
    template_variable_name = 'cultural_area'

    success_url = '/cultural_area/'

    keycloak_scopes = {
        'DEFAULT': 'cultural_area:update',
    }
