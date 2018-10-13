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
from telemeta_front.forms.location import LocationForm


class LocationAdd(FormView):
    template_name = "../templates/location-add.html"
    form_class = LocationForm
    success_url = '/location/'

    def post(self, request, *args, **kwargs):

        form = LocationForm(request.POST, initial={'name': u'Vendôme'})

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/location/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/location/')

            except RequestException:
                return HttpResponseRedirect('/location/add')

        return HttpResponseRedirect('/location/add')
