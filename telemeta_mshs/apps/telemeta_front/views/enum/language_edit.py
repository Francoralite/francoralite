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
from telemeta_front.forms.language import LanguageForm
from django.shortcuts import render
import telemeta_front.tools as tools


class LanguageEdit(FormView):
    template_name = "../templates/enum/language-add.html"
    form_class = LanguageForm
    success_url = '/language/'

    keycloak_scopes = {
            'GET': 'language:view',
            'POST': 'language:add',
            'PATCH': 'language:update',
            'PUT': 'language:update'}

    def get_context_data(self, **kwargs):
        try:
            context = super(LanguageEdit, self).get_context_data(**kwargs)
            id = kwargs.get('id')
            # Obtain values of the record
            context['language'] = tools.request_api(
                '/api/language/' + str(id))
        except Exception as err:
            context['language'] = {}
            context['error'] = err.message
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        language = requests.get(
            FRONT_HOST_URL + '/api/language/' + str(id))
        data = language.json()
        form = LanguageForm(initial=data)

        return render(request,
                      '../templates/enum/language-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = LanguageForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/language/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/language/edit' +
                                                str(id))
                return HttpResponseRedirect('/language/')

            except RequestException:
                raise Exception(response.status_code)
                return HttpResponseRedirect('/language/edit')

        return render(request,
                      '../templates/enum/language-add.html',
                      {'form': form,
                       'id': id})
