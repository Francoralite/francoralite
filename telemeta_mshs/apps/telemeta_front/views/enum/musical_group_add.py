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
from telemeta_front.forms.musical_group import MusicalGroupForm


class MusicalGroupAdd(FormView):
    template_name = "../templates/enum/musical_group-add.html"
    form_class = MusicalGroupForm
    success_url = '/musical_group/'

    def post(self, request, *args, **kwargs):

        form = MusicalGroupForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/musical_group/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/musical_group/')

            except RequestException:
                return HttpResponseRedirect('/musical_group/add')

        return HttpResponseRedirect('/musical_group/add')
