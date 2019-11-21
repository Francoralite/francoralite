# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class EmitVoxView(FrancoraliteTemplateView):
    template_name = "../templates/enum/emit_vox.html"

    keycloak_scopes = {'GET': 'emit_vox:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(EmitVoxView, self).get_context_data(**kwargs)
            context['emit_voxs'] = tools.request_api('/api/emit_vox')
        except Exception as err:
            context['emit_voxs'] = []
            context['error'] = err.message

        return context
