# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.civility import CivilityForm
import francoralite.apps.francoralite_front.tools as tools


class CivilityAdd(FormView):
    template_name = "../templates/enum/civility-add.html"
    form_class = CivilityForm
    success_url = '/civility/'

    keycloak_scopes = {
        'DEFAULT': 'civility:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('civility', CivilityForm, request, *args, **kwargs)
