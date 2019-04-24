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
from telemeta_front.forms.recording_context import RecordingContextForm


class RecordingContextAdd(FormView):
    template_name = "../templates/enum/recording_context-add.html"
    form_class = RecordingContextForm
    success_url = '/recording_context/'

    def post(self, request, *args, **kwargs):

        form = RecordingContextForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/recording_context/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/recording_context/')

            except RequestException:
                return HttpResponseRedirect('/recording_context/add')

        return HttpResponseRedirect('/recording_context/add')
