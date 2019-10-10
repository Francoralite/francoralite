# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from settings import FRONT_HOST_URL
from telemeta_front.forms.mission import MissionForm
import telemeta_front.tools as tools


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
        return tools.post('mission', MissionForm, request, *args, **kwargs)
