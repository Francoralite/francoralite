# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
import telemeta_front.tools as tools
from telemeta_front.forms.instrument import InstrumentForm


class InstrumentDetail(TemplateView):
    template_name = "../templates/enum/instrument-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(InstrumentDetail, self).get_context_data(**kwargs)
            context['instruments'] = tools.request_api(
                '/api/instrument/' + context['id'])
            context['form'] = InstrumentForm()
        except Exception as err:
            context['instruments'] = {}
            context['error'] = err.message
            context['form'] = InstrumentForm()
        return context
