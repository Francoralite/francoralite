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
from telemeta_front.forms.emit_vox import EmitVoxForm


class EmitVoxAdd(FormView):
    template_name = "../templates/enum/emit_vox-add.html"
    form_class = EmitVoxForm
    success_url = '/emit_vox/'

    def post(self, request, *args, **kwargs):

        form = EmitVoxForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/emit_vox/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/emit_vox/')

            except RequestException:
                return HttpResponseRedirect('/emit_vox/add')

        return HttpResponseRedirect('/emit_vox/add')
