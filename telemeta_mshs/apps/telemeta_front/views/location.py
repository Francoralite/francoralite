# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import requests
from django.conf import settings


class LocationView(FrancoraliteTemplateView):
    template_name = "../templates/location.html"

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['locations'] = requests.get(
            settings.FRONT_HOST_URL+'/api/location/').json
        return context
