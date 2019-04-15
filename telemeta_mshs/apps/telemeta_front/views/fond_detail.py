# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.base import TemplateView

from telemeta_front.forms.fond import FondForm
import telemeta_front.tools as tools


class FondDetail(TemplateView):
    template_name = "../templates/fond-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(FondDetail, self).get_context_data(**kwargs)
            # Obtain values of the record fond
            context['fond'] = tools.request_api(
                '/api/fond/' + context['id'])
            # Obtain values of related fonds
            context['missions'] = tools.request_api(
                '/api/mission/?fonds=' + context['id'])
        except Exception as err:
            context['fond'] = {}
            context['missions'] = []
            context['form'] = FondForm()
            context['error'] = err.message
        return context
