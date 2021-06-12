# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools


class RecordingContextView(FrancoraliteTemplateView):
    template_name = "../templates/enum/recording_context.html"

    keycloak_scopes = {'GET': 'recording_context:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(RecordingContextView, self).get_context_data(
                **kwargs)
            context['recording_contexts'] = tools.request_api(
                '/api/recordingcontext')
        except Exception as err:
            context['recording_contexts'] = []
            context['error'] = err.message

        return context
