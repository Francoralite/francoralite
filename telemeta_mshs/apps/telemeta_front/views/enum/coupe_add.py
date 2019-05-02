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
from telemeta_front.forms.coupe import CoupeForm


class CoupeAdd(FormView):
    template_name = "../templates/enum/coupe-add.html"
    form_class = CoupeForm
    success_url = '/coupe/'

    def post(self, request, *args, **kwargs):

        form = CoupeForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/coupe/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/coupe/')

            except RequestException:
                return HttpResponseRedirect('/coupe/add')

        return HttpResponseRedirect('/coupe/add')
