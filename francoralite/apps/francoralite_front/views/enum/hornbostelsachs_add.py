# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.hornbostelsachs import HornbostelsachsForm
from ... import tools as tools

class HornbostelsachsAdd(FormView):
    template_name = "../templates/enum/hornbostelsachs-add.html"
    form_class = HornbostelsachsForm
    success_url = '/hornbostelsachs/'
    
    keycloak_scopes = {
        'DEFAULT': 'hornbostelsachs:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post(
            'hornbostelsachs', HornbostelsachsForm, request, *args, **kwargs)
