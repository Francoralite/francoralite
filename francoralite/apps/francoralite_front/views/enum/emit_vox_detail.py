# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.emit_vox import EmitVoxForm
from ... import tools

class EmitVoxDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/emit_vox-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'emit_vox:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(EmitVoxDetail, self).get_context_data(**kwargs)
            context['emit_vox'] = tools.request_api(
                '/api/emit_vox/' + context['id'])
            context['form'] = EmitVoxForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cette nature d’émission vocale n’existe pas.'))
        except Exception as err:
            context['emit_vox'] = {}
            context['error'] = err
            context['form'] = EmitVoxForm()
        return context
