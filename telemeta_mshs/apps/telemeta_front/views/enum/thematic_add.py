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
from telemeta_front.forms.thematic import ThematicForm


class ThematicAdd(FormView):
    template_name = "../templates/enum/thematic-add.html"
    form_class = ThematicForm
    success_url = '/thematic/'

    def post(self, request, *args, **kwargs):

        form = ThematicForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/thematic/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/thematic/')

            except RequestException:
                return HttpResponseRedirect('/thematic/add')

        return HttpResponseRedirect('/thematic/add')
