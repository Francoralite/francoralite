# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.cultural_area import CulturalAreaForm
import francoralite.apps.francoralite_front.tools as tools


class CulturalAreaAdd(FormView):
    template_name = "../templates/enum/cultural_area-add.html"
    form_class = CulturalAreaForm
    success_url = '/cultural_area/'

    keycloak_scopes = {
        'DEFAULT': 'cultural_area:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('cultural_area', CulturalAreaForm, request, *args, **kwargs)
