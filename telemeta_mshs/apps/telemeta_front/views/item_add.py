# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.item import ItemForm


class ItemAdd(FormView):
    template_name = "../templates/item-add.html"
    form_class = ItemForm
    success_url = '/item/'

    def post(self, request, *args, **kwargs):

        form = ItemForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/item/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/item/')

            except RequestException:
                return HttpResponseRedirect('/item/add')

        return HttpResponseRedirect('/item/add')
