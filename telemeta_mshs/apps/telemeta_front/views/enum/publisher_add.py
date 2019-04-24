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
from telemeta_front.forms.publisher import PublisherForm


class PublisherAdd(FormView):
    template_name = "../templates/enum/publisher-add.html"
    form_class = PublisherForm
    success_url = '/publisher/'

    def post(self, request, *args, **kwargs):

        form = PublisherForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/publisher/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/publisher/')

            except RequestException:
                return HttpResponseRedirect('/publisher/add')

        return HttpResponseRedirect('/publisher/add')
