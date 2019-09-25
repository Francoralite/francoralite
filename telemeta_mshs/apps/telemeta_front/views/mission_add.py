# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from rest_framework import status
import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.mission import MissionForm


class MissionAdd(FormView):
    template_name = "../templates/mission-add.html"
    form_class = MissionForm
    success_url = '/mission/'

    def get_initial(self):
        initial = super(MissionAdd, self).get_initial()
        initial['fonds'] = self.kwargs['id_fond']
        # Obtain code of the fonds
        response = requests.get(
            FRONT_HOST_URL + '/api/fond/' + self.kwargs['id_fond'])
        if response.status_code == status.HTTP_200_OK:
            initial['code'] = response.json()['code']
        return initial

    def post(self, request, *args, **kwargs):
        id_institution = kwargs['id_institution']
        id_fond = kwargs['id_fond']
        form = MissionForm(request.POST)
        if form.is_valid():
            form.cleaned_data['description'] = form.data['descriptions']
            try:
                response = requests.post(
                    FRONT_HOST_URL + '/api/mission/',
                    data=form.cleaned_data
                )
                if response.status_code == status.HTTP_201_CREATED:
                    return HttpResponseRedirect('/mission/')

            except RequestException:
                return HttpResponseRedirect(
                    '/institution/' + id_institution + '/fond/'
                    + id_fond + '/mission/add')
        return HttpResponseRedirect(
            '/institution/' + id_institution + '/fond/'
            + id_fond + '/mission/add')
