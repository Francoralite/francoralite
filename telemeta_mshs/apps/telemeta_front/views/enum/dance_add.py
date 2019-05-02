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
from telemeta_front.forms.dance import DanceForm


class DanceAdd(FormView):
    template_name = "../templates/enum/dance-add.html"
    form_class = DanceForm
    success_url = '/dance/'

    def post(self, request, *args, **kwargs):

        form = DanceForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/dance/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/dance/')

            except RequestException:
                return HttpResponseRedirect('/dance/add')

        return HttpResponseRedirect('/dance/add')
