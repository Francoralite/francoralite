# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.recording_context import RecordingContextForm
from ... import tools


class RecordingContextDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/recording_context-detail.html"

    keycloak_scopes = {
        'DEFAULT': 'recording_context:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(RecordingContextDetail, self).get_context_data(
                **kwargs)
            context['recording_context'] = tools.request_api(
                '/api/recordingcontext/' + context['id'])
            context['form'] = RecordingContextForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cet éditeur n’existe pas.'))
        except Exception as err:
            context['recording_context'] = {}
            context['error'] = err
            context['form'] = RecordingContextForm()
        return context
