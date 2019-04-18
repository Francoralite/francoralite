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
from telemeta_front.forms.domain_vocal import DomainVocalForm
from django.shortcuts import render


class DomainVocalEdit(FormView):
    template_name = "../templates/enum/domain_vocal-add.html"
    form_class = DomainVocalForm
    success_url = '/domain_vocal/'

    def get_context_data(self, **kwargs):
        context = super(DomainVocalEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/domain_vocal/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['domain_vocal'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        domain_vocal = requests.get(
            FRONT_HOST_URL + '/api/domain_vocal/' + str(id))
        form = DomainVocalForm(initial=domain_vocal.json())

        return render(request,
                      '../templates/enum/domain_vocal-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = DomainVocalForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/domain_vocal/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/domain_vocal/edit' + str(id)
                                                + '/')
                return HttpResponseRedirect('/domain_vocal/')

            except RequestException:
                return HttpResponseRedirect('/domain_vocal/edit')

        return HttpResponseRedirect('/domain_vocal/edit')
