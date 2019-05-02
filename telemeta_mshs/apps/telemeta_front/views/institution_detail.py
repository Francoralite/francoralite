# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class InstitutionDetail(FrancoraliteTemplateView):
    template_name = "../templates/institution-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(InstitutionDetail, self).get_context_data(**kwargs)
            # Obtain values of the record institution
            context['institution'] = tools.request_api(
                '/api/institution/' + context['id'])
            # Obtain values of related fonds
            context['fonds'] = tools.request_api(
                '/api/fond/?institution=' + context['id'])
        except Exception as err:
            context['institution'] = {}
            context['fonds'] = []
            context['error'] = err.message
        return context
