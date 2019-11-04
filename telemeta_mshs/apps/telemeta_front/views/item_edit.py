# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.edit import FormView
from rest_framework import status
import requests
from settings import FRONT_HOST_URL
from telemeta_front.forms.item import ItemForm
from django.shortcuts import render
import telemeta_front.tools as tools


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
        form.fields['file'].required = False

        # Obtain gaphers of the record
        graphers = []
        response = requests.get(
            FRONT_HOST_URL+'/api/timeside/'
            + str(id) + '/visualize/')
        if response.status_code == status.HTTP_200_OK:
            graphers.append(response.json)

        return render(request,
                      '../templates/item-add.html',
                      {'form': form, 'id': id, 'item': item.json(),
                       'graphers': graphers})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'item', ItemForm, request, *args, **kwargs)
