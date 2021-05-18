# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from telemeta_mshs.apps.telemeta_front.forms.recording_context import RecordingContextForm
import telemeta_mshs.apps.telemeta_front.tools as tools


class RecordingContextDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/recording_context-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(RecordingContextDetail, self).get_context_data(
                **kwargs)
            context['recording_context'] = tools.request_api(
                '/api/recordingcontext/' + context['id'])
            context['form'] = RecordingContextForm()

        except Exception as err:
            context['recording_context'] = {}
            context['error'] = err.message
            context['form'] = RecordingContextForm()
        return context
