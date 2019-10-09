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
from telemeta_front.forms.location import LocationForm
from django.shortcuts import render
import telemeta_front.tools as tools


class LocationEdit(FormView):
    template_name = "../templates/location-add.html"
    form_class = LocationForm
    success_url = '/location/'

    def get_context_data(self, **kwargs):
        context = super(LocationEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/location/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['location'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        location = requests.get(
            FRONT_HOST_URL + '/api/location/' + str(id))
        form = LocationForm(initial=location.json())

        return render(request,
                      '../templates/location-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch('location', LocationForm, request, *args, **kwargs)
