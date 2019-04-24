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
from telemeta_front.forms.hornbostelsachs import HornbostelsachsForm


class HornbostelsachsAdd(FormView):
    template_name = "../templates/enum/hornbostelsachs-add.html"
    form_class = HornbostelsachsForm
    success_url = '/hornbostelsachs/'

    def post(self, request, *args, **kwargs):

        form = HornbostelsachsForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/hornbostelsachs/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/hornbostelsachs/')

            except RequestException:
                return HttpResponseRedirect('/hornbostelsachs/add')

        return HttpResponseRedirect('/hornbostelsachs/add')
