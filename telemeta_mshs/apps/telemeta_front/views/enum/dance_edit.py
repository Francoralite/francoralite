# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from telemeta_front.forms.dance import DanceForm
from django.shortcuts import render
import telemeta_front.tools as tools


class DanceEdit(FormView):
    template_name = "../templates/enum/dance-add.html"
    form_class = DanceForm
    success_url = '/dance/'

    def get_context_data(self, **kwargs):
        context = super(DanceEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/dance/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['dance'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        dance = requests.get(
            settings.FRONT_HOST_URL + '/api/dance/' + str(id))
        form = DanceForm(initial=dance.json())

        return render(request,
                      '../templates/enum/dance-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch('dance', DanceForm, request, *args, **kwargs)
