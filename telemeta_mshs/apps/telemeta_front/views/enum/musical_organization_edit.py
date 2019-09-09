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
from telemeta_front.forms.musical_organization import MusicalOrganizationForm
from django.shortcuts import render


class MusicalOrganizationEdit(FormView):
    template_name = "../templates/enum/musical_organization-add.html"
    form_class = MusicalOrganizationForm
    success_url = '/musical_organization/'

    def get_context_data(self, **kwargs):
        context = super(
            MusicalOrganizationEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/musical_organization/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['musical_organization'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        musical_organization = requests.get(
            FRONT_HOST_URL + '/api/musical_organization/' + str(id))
        form = MusicalOrganizationForm(initial=musical_organization.json())

        return render(request,
                      '../templates/enum/musical_organization-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = MusicalOrganizationForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL +
                    '/api/musical_organization/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/musical_organization/edit/' +
                                                str(id))
                return HttpResponseRedirect('/musical_organization/')

            except RequestException:
                return HttpResponseRedirect('/musical_organization/edit')

        return HttpResponseRedirect('/musical_organization/edit')
