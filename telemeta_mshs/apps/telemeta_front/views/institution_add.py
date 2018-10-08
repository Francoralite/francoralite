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
from telemeta_front.forms.institution import InstitutionForm


class InstitutionAdd(FormView):
    template_name = "../templates/institution-add.html"
    form_class = InstitutionForm
    success_url = '/institution/'

    def post(self, request, *args, **kwargs):

        form = InstitutionForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/institution/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/institution/')

            except RequestException:
                return HttpResponseRedirect('/institution/add')

        return HttpResponseRedirect('/institution/add')
