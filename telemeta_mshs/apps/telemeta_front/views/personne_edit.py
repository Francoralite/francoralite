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
from telemeta_front.forms.personne import PersonneForm
from django.shortcuts import render


class PersonneEdit(FormView):
    template_name = "../templates/personne-add.html"
    form_class = PersonneForm
    success_url = '/authority/'

    def get_context_data(self, **kwargs):
        context = super(PersonneEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/authority/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['personne'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        personne = requests.get(
            FRONT_HOST_URL + '/api/authority/' + str(id))
        form = PersonneForm(initial=personne.json())

        return render(request,
                      '../templates/personne-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = PersonneForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/authority/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/authority/edit/' +
                                                str(id) + '/')
                return HttpResponseRedirect('/authority/')

            except RequestException:
                raise Exception(response.status_code)
                return HttpResponseRedirect('/authority/edit/')
        raise Exception(3)
        return HttpResponseRedirect('/authority/edit/')
