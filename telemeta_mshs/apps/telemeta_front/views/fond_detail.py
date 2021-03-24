# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView

from telemeta_mshs.apps.telemeta_front.forms.fond import FondForm
import telemeta_mshs.apps.telemeta_front.tools as tools


class FondDetail(FrancoraliteTemplateView):
    template_name = "../templates/fond-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(FondDetail, self).get_context_data(**kwargs)
            # Obtain values of the record fond
            context['form'] = FondForm()
            context['fond'] = tools.request_api(
                '/api/fond/' + context['id'])
            # Obtain values of related fonds
            context['missions'] = tools.request_api(
                '/api/mission?fonds=' + context['id'])
            # Obtain values of related informers
            context['informers'] = tools.request_api(
                '/api/fond/' + context['id'] + '/informers')
            # Obtain values of related collectors
            context['collectors'] = tools.request_api(
                '/api/fond/' + context['id'] + '/collectors')
            # Obtain values of related documents
            context['documents'] = tools.request_api(
                '/api/fond/' + context['id'] + '/document')
            # Obtain values of the start and en dates of related collections
            context['dates'] = tools.request_api(
                '/api/fond/' + context['id'] + '/dates')
        except Exception as err:
            context['fond'] = {}
            context['missions'] = []
            context['informers'] = []
            context['collectors'] = []
            context['documents'] = []
            context['dates'] = ['', '']
            context['error'] = err.message
        return context
