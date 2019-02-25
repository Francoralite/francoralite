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
from telemeta_front.forms.item import ItemForm
from django.shortcuts import render


class ItemEdit(FormView):
    template_name = "../templates/item-add.html"
    form_class = ItemForm
    success_url = '/item/'

    def get_context_data(self, **kwargs):
        context = super(ItemEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/item/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['item'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        item = requests.get(
            FRONT_HOST_URL + '/api/item/' + str(id))
        form = ItemForm(initial=item.json())

        return render(request,
                      '../templates/item-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = ItemForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/item/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/item/edit' +
                                                str(id) + '/')
                return HttpResponseRedirect('/item/')

            except RequestException:
                return HttpResponseRedirect('/item/edit')

        return HttpResponseRedirect('/item/edit')
