# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.edit import FormView
from rest_framework import status
import requests
from settings import FRONT_HOST_URL
from telemeta_front.forms.coupe import CoupeForm
from django.shortcuts import render
import telemeta_front.tools as tools


class CoupeEdit(FormView):
    template_name = "../templates/enum/coupe-add.html"
    form_class = CoupeForm
    success_url = '/coupe/'

    def get_context_data(self, **kwargs):
        context = super(CoupeEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/coupe/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['coupe'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        coupe = requests.get(
            FRONT_HOST_URL + '/api/coupe/' + str(id))
        form = CoupeForm(initial=coupe.json())

        return render(request,
                      '../templates/enum/coupe-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch('coupe', CoupeForm, request, *args, **kwargs)
