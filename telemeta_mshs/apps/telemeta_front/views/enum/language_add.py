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
from telemeta_front.forms.language import LanguageForm


class LanguageAdd(FormView):
    template_name = "../templates/enum/language-add.html"
    form_class = LanguageForm
    success_url = '/language/'

    def post(self, request, *args, **kwargs):

        form = LanguageForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/language/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/language/')

            except RequestException:
                return HttpResponseRedirect('/language/add')

        return HttpResponseRedirect('/language/add')
