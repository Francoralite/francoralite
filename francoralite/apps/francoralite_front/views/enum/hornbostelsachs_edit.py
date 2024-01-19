# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.hornbostelsachs import HornbostelsachsForm


class HornbostelsachsEdit(FrancoraliteFormView):
    template_name = "../templates/enum/hornbostelsachs-add.html"
    api_url_prefix = '/api/hornbostelsachs/'
    entity_name = 'hornbostelsachs'
    form_class = HornbostelsachsForm
    template_variable_name = 'hornbostelsachs'
    success_url = '/hornbostelsachs/'

    keycloak_scopes = {
        'DEFAULT': 'hornbostelsachs:update',
    }
