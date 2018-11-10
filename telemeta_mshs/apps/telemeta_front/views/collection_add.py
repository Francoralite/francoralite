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
from telemeta_front.forms.collection import CollectionForm


class CollectionAdd(FormView):
    template_name = "../templates/collection-add.html"
    form_class = CollectionForm
    success_url = '/collection/'

    def get_initial(self):
        initial = super(CollectionAdd, self).get_initial()
        initial['mission'] = self.kwargs['id_mission']
        return initial

    def post(self, request, *args, **kwargs):
        raise Exception(1)
        form = CollectionForm(request.POST)
        raise Exception(1)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/collection/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/collection/')

            except RequestException:
                return HttpResponseRedirect('/collection/add')

        return HttpResponseRedirect('/collection/add')
