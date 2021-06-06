# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.mission import MissionForm
from django.shortcuts import render
import francoralite.apps.francoralite_front.tools as tools


class MissionEdit(FormView):
    template_name = "../templates/mission-add.html"
    form_class = MissionForm
    success_url = '/mission/'

    def get_context_data(self, **kwargs):
        context = super(MissionEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/mission/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['mission'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        mission = requests.get(
            settings.FRONT_HOST_URL + '/api/mission/' + str(id))
        data = mission.json()
        data['fonds'] = data['fonds']['id']
        form = MissionForm(initial=data)

        return render(request,
                      '../templates/mission-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch('mission', MissionForm, request, *args, **kwargs)
