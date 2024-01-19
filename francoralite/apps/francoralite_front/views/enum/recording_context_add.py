# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.recording_context import RecordingContextForm
from ... import tools as tools


class RecordingContextAdd(FormView):
    template_name = "../templates/enum/recording_context-add.html"
    form_class = RecordingContextForm
    success_url = '/recording_context/'
    
    keycloak_scopes = {
        'DEFAULT': 'recording_context:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post(
            'recording_context',
            RecordingContextForm, request, *args, **kwargs)
