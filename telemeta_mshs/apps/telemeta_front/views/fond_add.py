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
from telemeta_front.forms.fond import FondForm


class FondAdd(FormView):
    template_name = "../templates/fond-add.html"
    form_class = FondForm
    success_url = '/fond/'

    def form_valid(self, form):
        form.cleaned_data['description'] = form.data['descriptions']
        if form.is_valid():
            requests.post(
                FRONT_HOST_URL + '/api/fond/',
                data=form.cleaned_data
            )
        return super(FondAdd, self).form_valid(form)
    # def post(self, request, *args, **kwargs):
    #
    #     form = FondForm(request.POST)
    #
    #     if form.is_valid():
    #
    #         try:
    #             requests.post(
    #                 FRONT_HOST_URL + '/api/fond/',
    #                 data=form.cleaned_data
    #             )
    #             return HttpResponseRedirect('/fond/')
    #
    #         except RequestException:
    #             return HttpResponseRedirect('/fond/add')
    #
    #     return HttpResponseRedirect('/fond/add')
