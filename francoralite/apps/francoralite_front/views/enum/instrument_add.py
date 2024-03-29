# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.instrument import InstrumentForm
from ... import tools as tools


class InstrumentAdd(FormView):
    template_name = "../templates/enum/instrument-add.html"
    form_class = InstrumentForm
    success_url = '/instrument/'
    
    keycloak_scopes = {
        'DEFAULT': 'instrument:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post(
            'instrument', InstrumentForm, request, *args, **kwargs)
