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
from telemeta_front.forms.domain_song import DomainSongForm


class DomainSongAdd(FormView):
    template_name = "../templates/enum/domain_song-add.html"
    form_class = DomainSongForm
    success_url = '/domain_song/'

    def post(self, request, *args, **kwargs):

        form = DomainSongForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/domain_song/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/domain_song/')

            except RequestException:
                return HttpResponseRedirect('/domain_song/add')

        return HttpResponseRedirect('/domain_song/add')
