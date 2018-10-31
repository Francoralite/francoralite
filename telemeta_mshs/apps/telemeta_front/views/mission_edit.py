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
from django.shortcuts import render


class MissionEdit(FormView):
    template_name = "../templates/mission-add.html"
    form_class = MissionForm
    success_url = '/mission/'

    def get_context_data(self, **kwargs):
        context = super(MissionEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/mission/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['mission'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        mission = requests.get(
            FRONT_HOST_URL + '/api/mission/' + str(id))
        form = MissionForm(initial=mission.json())

        return render(request,
                      '../templates/mission-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = MissionForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/mission/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/mission/edit' +
                                                str(id) + '/')
                return HttpResponseRedirect('/mission/')

            except RequestException:
                return HttpResponseRedirect('/mission/edit')

        return HttpResponseRedirect('/mission/edit')
