# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from telemeta_mshs.apps.telemeta_front.forms.emit_vox import EmitVoxForm
import telemeta_mshs.apps.telemeta_front.tools as tools


class EmitVoxDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/emit_vox-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(EmitVoxDetail, self).get_context_data(**kwargs)
            context['emit_vox'] = tools.request_api(
                '/api/emit_vox/' + context['id'])
            context['form'] = EmitVoxForm()

        except Exception as err:
            context['emit_vox'] = {}
            context['error'] = err.message
            context['form'] = EmitVoxForm()
        return context
