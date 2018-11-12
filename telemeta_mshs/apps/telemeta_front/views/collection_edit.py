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
from telemeta_front.forms.collection import CollectionForm
from django.shortcuts import render


class CollectionEdit(FormView):
    template_name = "../templates/collection-add.html"
    form_class = CollectionForm
    success_url = '/extcollection/'

    def get_context_data(self, **kwargs):
        context = super(CollectionEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/extcollection/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['collection'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        collection = requests.get(
            FRONT_HOST_URL + '/api/collection/' + str(id))
        data = collection.json()
        data['mission'] = data['mission']['id']
        form = CollectionForm(initial=data)

        return render(request,
                      '../templates/collection-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = CollectionForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/collection/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect(
                        '/collection/edit/' + str(id))
                return HttpResponseRedirect('/collection/')

            except RequestException:
                return HttpResponseRedirect('/collection/edit')

        return HttpResponseRedirect('/collection/edit')
