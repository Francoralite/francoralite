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
from telemeta_front.forms.musical_organization import MusicalOrganizationForm


class MusicalOrganizationAdd(FormView):
    template_name = "../templates/enum/musical_organization-add.html"
    form_class = MusicalOrganizationForm
    success_url = '/musical_organization/'

    def post(self, request, *args, **kwargs):

        form = MusicalOrganizationForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/musical_organization/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/musical_organization/')

            except RequestException:
                return HttpResponseRedirect('/musical_organization/add')

        return HttpResponseRedirect('/musical_organization/add')
