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
from telemeta_front.forms.instrument import InstrumentForm


class InstrumentAdd(FormView):
    template_name = "../templates/enum/instrument-add.html"
    form_class = InstrumentForm
    success_url = '/instrument/'

    def post(self, request, *args, **kwargs):

        form = InstrumentForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/instrument/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/instrument/')

            except RequestException:
                return HttpResponseRedirect('/instrument/add')

        return HttpResponseRedirect('/instrument/add')
