# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.emit_vox import EmitVoxForm
import francoralite.apps.francoralite_front.tools as tools


class EmitVoxAdd(FormView):
    template_name = "../templates/enum/emit_vox-add.html"
    form_class = EmitVoxForm
    success_url = '/emit_vox/'

    def post(self, request, *args, **kwargs):
        return tools.post('emit_vox', EmitVoxForm, request, *args, **kwargs)
