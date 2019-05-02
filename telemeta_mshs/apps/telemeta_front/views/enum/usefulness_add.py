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
from telemeta_front.forms.usefulness import UsefulnessForm


class UsefulnessAdd(FormView):
    template_name = "../templates/enum/usefulness-add.html"
    form_class = UsefulnessForm
    success_url = '/usefulness/'

    def post(self, request, *args, **kwargs):

        form = UsefulnessForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/usefulness/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/usefulness/')

            except RequestException:
                return HttpResponseRedirect('/usefulness/add')

        return HttpResponseRedirect('/usefulness/add')
