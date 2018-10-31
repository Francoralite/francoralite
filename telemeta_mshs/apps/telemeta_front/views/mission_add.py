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
from telemeta_front.forms.mission import MissionForm


class MissionAdd(FormView):
    template_name = "../templates/mission-add.html"
    form_class = MissionForm
    success_url = '/mission/'

    def post(self, request, *args, **kwargs):

        form = MissionForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/mission/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/mission/')

            except RequestException:
                return HttpResponseRedirect('/mission/add')

        return HttpResponseRedirect('/mission/add')
