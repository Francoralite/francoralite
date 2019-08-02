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
import telemeta_front.tools as tools


class PersonneEdit(FormView):
    template_name = "../templates/personne-add.html"
    form_class = PersonneForm
    success_url = '/authority/'

    keycloak_scopes = {
            'GET': 'authority:view',
            'POST': 'authority:add',
            'PATCH': 'authority:update',
            'PUT': 'authority:update'}

    def get_context_data(self, **kwargs):
        try:
            context = super(PersonneEdit, self).get_context_data(**kwargs)
            id = kwargs.get('id')
            # Obtain values of the record
            context['personne'] = tools.request_api(
                '/api/authority/' + str(id))
        except Exception as err:
            context['personne'] = {}
            context['error'] = err.message
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        personne = requests.get(
            FRONT_HOST_URL + '/api/authority/' + str(id))
        data = personne.json()
        form = PersonneForm(initial=data)
        # authority = personne.json()

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
                                                str(id))
                return HttpResponseRedirect('/authority/')
            except RequestException:
                raise Exception(response.status_code)
                return HttpResponseRedirect('/authority/edit/')
        return render(request,
                      '../templates/personne-add.html',
                      {'form': form,
                       'id': id})
