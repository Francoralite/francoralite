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
from telemeta_front.forms.personne import PersonneForm


class PersonneAdd(FormView):
    template_name = "../templates/personne-add.html"
    form_class = PersonneForm
    success_url = '/personne/'

    def post(self, request, *args, **kwargs):

        form = PersonneForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/personne/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/personne/')

            except RequestException:
                return HttpResponseRedirect('/personne/add')

        return HttpResponseRedirect('/personne/add')
