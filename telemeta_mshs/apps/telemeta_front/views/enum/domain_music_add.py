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
from telemeta_front.forms.domain_music import DomainMusicForm


class DomainMusicAdd(FormView):
    template_name = "../templates/enum/domain_music-add.html"
    form_class = DomainMusicForm
    success_url = '/domain_music/'

    def post(self, request, *args, **kwargs):

        form = DomainMusicForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/domain_music/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/domain_music/')

            except RequestException:
                return HttpResponseRedirect('/domain_music/add')

        return HttpResponseRedirect('/domain_music/add')
