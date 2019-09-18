# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
import requests
from requests.exceptions import RequestException
from rest_framework import status
from settings import FRONT_HOST_URL
from telemeta_front.forms.item import ItemForm
from related import write_relations, query_related
from rest_framework.parsers import MultiPartParser, FormParser


class ItemAdd(FormView):
    template_name = "../templates/item-add.html"
    form_class = ItemForm
    parser_classes = (MultiPartParser, FormParser)
    success_url = '/item/'

    def get_initial(self):
        initial = super(ItemAdd, self).get_initial()
        initial['collection'] = self.kwargs['id_collection']
        # Obtain code of the mission
        response = requests.get(
            FRONT_HOST_URL + '/api/collection/' + self.kwargs['id_collection'])
        if response.status_code == status.HTTP_200_OK:
            initial['code'] = response.json()['code']
        return initial

    def post(self, request, *args, **kwargs):
        id_institution = kwargs['id_institution']
        id_fond = kwargs['id_fond']
        id_mission = kwargs['id_mission']
        id_collection = kwargs['id_collection']

        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Remove the 'file' entry : if not, there some bugs
                del form.cleaned_data['file']
                response = requests.post(
                    FRONT_HOST_URL + '/api/item/',
                    data=form.cleaned_data,  files=request.FILES
                )
                if response.status_code == status.HTTP_201_CREATED:
                    item = response.json()

            except RequestException:
                return super(ItemAdd, self).form_valid(form)
        return super(ItemAdd, self).form_valid(form)
        # return HttpResponseRedirect(
        #     '/institution/' + id_institution + '/fond/'
        #     + id_fond + '/mission/' + id_mission + '/collection/'
        #     + id_collection + '/item/add')
