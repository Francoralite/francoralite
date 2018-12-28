# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.base import TemplateView
import requests
from settings import FRONT_HOST_URL


class InstrumentView(TemplateView):
    template_name = "../templates/enum/instrument.html"

    def get_context_data(self, **kwargs):
        context = super(InstrumentView, self).get_context_data(**kwargs)
        context['instruments'] = requests.get(
            FRONT_HOST_URL+'/api/instrument/').json
        return context
