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
from telemeta_front.forms.domain_tale import DomainTaleForm


class DomainTaleAdd(FormView):
    template_name = "../templates/enum/domain_tale-add.html"
    form_class = DomainTaleForm
    success_url = '/domain_tale/'

    def post(self, request, *args, **kwargs):

        form = DomainTaleForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/domain_tale/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/domain_tale/')

            except RequestException:
                return HttpResponseRedirect('/domain_tale/add')

        return HttpResponseRedirect('/domain_tale/add')
