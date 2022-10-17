# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.coupe import CoupeForm
import francoralite.apps.francoralite_front.tools as tools


class CoupeAdd(FormView):
    template_name = "../templates/enum/coupe-add.html"
    form_class = CoupeForm
    success_url = '/coupe/'

    keycloak_scopes = {
        'DEFAULT': 'coupe:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('coupe', CoupeForm, request, *args, **kwargs)
