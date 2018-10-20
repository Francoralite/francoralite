# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.location_gis import LocationForm


class LocationAdd(FormView):
    template_name = "../templates/location-add.html"
    form_class = LocationForm
    success_url = '/location_gis/'

    def post(self, request, *args, **kwargs):

        form = LocationForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/locationgis/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/location_gis/')

            except RequestException:
                return HttpResponseRedirect('/location_gis/add')

        return HttpResponseRedirect('/location_gis/add')
