# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.emit_vox import EmitVoxForm


class EmitVoxEdit(FrancoraliteFormView):
    template_name = "../templates/enum/emit_vox-add.html"
    api_url_prefix = '/api/emit_vox/'
    entity_name = 'emit_vox'
    form_class = EmitVoxForm
    template_variable_name = 'emit_vox'
    success_url = '/emit_vox/'
