# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from rest_framework import status
import requests

from django.conf import settings
from telemeta_mshs.apps.telemeta_front.forms.location import LocationForm


class LocationDetail(FrancoraliteTemplateView):
    template_name = "../templates/location-detail.html"

    def get_context_data(self, **kwargs):
        context = super(LocationDetail, self).get_context_data(**kwargs)

        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/location/' + context['id'])
        if response.status_code == status.HTTP_200_OK:
            context['location'] = response.json
            context['form'] = LocationForm
        return context
