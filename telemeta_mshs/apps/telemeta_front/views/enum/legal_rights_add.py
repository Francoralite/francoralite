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
from telemeta_front.forms.legal_rights import LegalRightsForm


class LegalRightsAdd(FormView):
    template_name = "../templates/enum/legal_rights-add.html"
    form_class = LegalRightsForm
    success_url = '/legal_rights/'

    def post(self, request, *args, **kwargs):

        form = LegalRightsForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/legalrights/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/legal_rights/')

            except RequestException:
                return HttpResponseRedirect('/legal_rights/add')

        return HttpResponseRedirect('/legal_rights/add')
