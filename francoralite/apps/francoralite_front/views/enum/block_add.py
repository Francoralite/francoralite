# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.block import BlockForm
import francoralite.apps.francoralite_front.tools as tools


class BlockAdd(FormView):
    template_name = '../templates/enum/block-add.html'
    form_class = BlockForm
    success_url = '/block/'

    keycloak_scopes = {
        'DEFAULT': 'block:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('block', BlockForm, request, *args, **kwargs)
