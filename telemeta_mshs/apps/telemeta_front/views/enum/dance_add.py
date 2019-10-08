# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.dance import DanceForm
import telemeta_front.tools as tools


class DanceAdd(FormView):
    template_name = "../templates/enum/dance-add.html"
    form_class = DanceForm
    success_url = '/dance/'

    def post(self, request, *args, **kwargs):

        form = DanceForm(request.POST)

        if form.is_valid():
            try:
                tools.post_api(FRONT_HOST_URL + '/api/dance/',
                               data=form.cleaned_data,
                               request=request)
                return HttpResponseRedirect('/dance/')

            except RequestException:
                return HttpResponseRedirect('/dance/add')

        return HttpResponseRedirect('/dance/add')
