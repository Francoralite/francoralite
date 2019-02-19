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
from telemeta_front.forms.musical_group import MusicalGroupForm
from django.shortcuts import render


class MusicalGroupEdit(FormView):
    template_name = "../templates/enum/musical_group-add.html"
    form_class = MusicalGroupForm
    success_url = '/musical_group/'

    def get_context_data(self, **kwargs):
        context = super(MusicalGroupEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/musical_group/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['musical_group'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        musical_group = requests.get(
            FRONT_HOST_URL + '/api/musical_group/' + str(id))
        form = MusicalGroupForm(initial=musical_group.json())

        return render(request,
                      '../templates/enum/musical_group-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = MusicalGroupForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/musical_group/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/musical_group/edit' +
                                                str(id) + '/')
                return HttpResponseRedirect('/musical_group/')

            except RequestException:
                return HttpResponseRedirect('/musical_group/edit')

        return HttpResponseRedirect('/musical_group/edit')
