# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools
from telemeta_front.forms.mission import MissionForm


class MissionDetail(FrancoraliteTemplateView):
    template_name = "../templates/mission-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(MissionDetail, self).get_context_data(**kwargs)
            # Obtain values of the record mission
            context['mission'] = tools.request_api(
                '/api/mission/' + context['id'])
            # Obtain values of related collections
            context['collections'] = tools.request_api(
                '/api/collection/?mission=' + context['id'])
            # Obtain values of related informers
            context['informers'] = tools.request_api(
                '/api/mission/' + context['id'] + '/informers/')
            # Obtain values of related collectors
            context['collectors'] = tools.request_api(
                '/api/mission/' + context['id'] + '/collectors/')
            context['form'] = MissionForm()
        except Exception as err:
            context['mission'] = {}
            context['collections'] = []
            context['informers'] = []
            context['collectors'] = []
            context['error'] = err.message
        return context
