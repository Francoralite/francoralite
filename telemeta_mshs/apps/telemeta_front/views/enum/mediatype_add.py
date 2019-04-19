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
from telemeta_front.forms.mediatype import MediaTypeForm


class MediaTypeAdd(FormView):
    template_name = "../templates/enum/mediatype-add.html"
    form_class = MediaTypeForm
    success_url = '/mediatype/'

    def post(self, request, *args, **kwargs):

        form = MediaTypeForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/mediatype/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/mediatype/')

            except RequestException:
                return HttpResponseRedirect('/mediatype/add')

        return HttpResponseRedirect('/mediatype/add')
