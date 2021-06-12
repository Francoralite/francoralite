# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.usefulness import UsefulnessForm
from django.shortcuts import render
import francoralite.apps.francoralite_front.tools as tools


class UsefulnessEdit(FormView):
    template_name = "../templates/enum/usefulness-add.html"
    form_class = UsefulnessForm
    success_url = '/usefulness/'

    def get_context_data(self, **kwargs):
        context = super(UsefulnessEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/usefulness/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['usefulness'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        usefulness = requests.get(
            settings.FRONT_HOST_URL + '/api/usefulness/' + str(id))
        form = UsefulnessForm(initial=usefulness.json())

        return render(request,
                      '../templates/enum/usefulness-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'usefulness', UsefulnessForm, request, *args, **kwargs)
