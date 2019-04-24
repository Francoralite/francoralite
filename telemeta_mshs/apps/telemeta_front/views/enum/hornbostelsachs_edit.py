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
from telemeta_front.forms.hornbostelsachs import HornbostelsachsForm
from django.shortcuts import render


class HornbostelsachsEdit(FormView):
    template_name = "../templates/enum/hornbostelsachs-add.html"
    form_class = HornbostelsachsForm
    success_url = '/hornbostelsachs/'

    def get_context_data(self, **kwargs):
        context = super(HornbostelsachsEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/hornbostelsachs/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['hornbostelsachs'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        hornbostelsachs = requests.get(
            FRONT_HOST_URL + '/api/hornbostelsachs/' + str(id))
        form = HornbostelsachsForm(initial=hornbostelsachs.json())

        return render(request,
                      '../templates/enum/hornbostelsachs-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = HornbostelsachsForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/hornbostelsachs/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/hornbostelsachs/edit' + str(
                        id)
                                                + '/')
                return HttpResponseRedirect('/hornbostelsachs/')

            except RequestException:
                return HttpResponseRedirect('/hornbostelsachs/edit')

        return HttpResponseRedirect('/hornbostelsachs/edit')
