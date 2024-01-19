# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.dance import DanceForm
from ... import tools as tools


class DanceAdd(FormView):
    template_name = "../templates/enum/dance-add.html"
    form_class = DanceForm
    success_url = '/dance/'

    keycloak_scopes = {
        'DEFAULT': 'dance:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('dance', DanceForm, request, *args, **kwargs)
