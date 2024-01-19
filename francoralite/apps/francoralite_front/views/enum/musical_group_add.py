# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.musical_group import MusicalGroupForm
from ... import tools as tools


class MusicalGroupAdd(FormView):
    template_name = "../templates/enum/musical_group-add.html"
    form_class = MusicalGroupForm
    success_url = '/musical_group/'
    
    keycloak_scopes = {
        'DEFAULT': 'musical_group:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post(
            'musical_group', MusicalGroupForm, request, *args, **kwargs)
