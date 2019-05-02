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
from telemeta_front.forms.publisher import PublisherForm
from django.shortcuts import render


class PublisherEdit(FormView):
    template_name = "../templates/enum/publisher-add.html"
    form_class = PublisherForm
    success_url = '/publisher/'

    def get_context_data(self, **kwargs):
        context = super(PublisherEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/publisher/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['publisher'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        publisher = requests.get(
            FRONT_HOST_URL + '/api/publisher/' + str(id))
        form = PublisherForm(initial=publisher.json())

        return render(request,
                      '../templates/enum/publisher-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = PublisherForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/publisher/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/publisher/edit' + str(id)
                                                + '/')
                return HttpResponseRedirect('/publisher/')

            except RequestException:
                return HttpResponseRedirect('/publisher/edit')

        return HttpResponseRedirect('/publisher/edit')
