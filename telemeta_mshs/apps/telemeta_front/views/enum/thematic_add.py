# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.thematic import ThematicForm
import telemeta_front.tools as tools


class ThematicAdd(FormView):
    template_name = "../templates/enum/thematic-add.html"
    form_class = ThematicForm
    success_url = '/thematic/'

    def post(self, request, *args, **kwargs):

        form = ThematicForm(request.POST)

        if form.is_valid():

            try:
                tools.post_api(
                    FRONT_HOST_URL + '/api/thematic/',
                    data=form.cleaned_data,
                    request=request
                )
                return HttpResponseRedirect('/thematic/')

            except RequestException:
                return HttpResponseRedirect('/thematic/add')

        return HttpResponseRedirect('/thematic/add')
