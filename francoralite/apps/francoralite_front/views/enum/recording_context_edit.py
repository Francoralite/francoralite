# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.recording_context import RecordingContextForm


class RecordingContextEdit(FrancoraliteFormView):
    template_name = "../templates/enum/recording_context-add.html"
    form_class = RecordingContextForm
    api_url_prefix = '/api/recordingcontext/'
    entity_name = 'recording_context'
    template_variable_name = 'recording_context'
    success_url = '/recordingcontext/'

    keycloak_scopes = {
        'DEFAULT': 'recording_context:update',
    }
