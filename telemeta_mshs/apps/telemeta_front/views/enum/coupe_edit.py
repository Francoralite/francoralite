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
from telemeta_front.forms.coupe import CoupeForm
from django.shortcuts import render


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

        form = CoupeForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/coupe/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/coupe/edit' + str(id)
                                                + '/')
                return HttpResponseRedirect('/coupe/')

            except RequestException:
                return HttpResponseRedirect('/coupe/edit')

        return HttpResponseRedirect('/coupe/edit')
