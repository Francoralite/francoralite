# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
from rest_framework import status
import requests

from settings import FRONT_HOST_URL
from telemeta_front.forms.domain_song import DomainSongForm


class DomainSongDetail(TemplateView):
    template_name = "../templates/enum/domain_song-detail.html"

    def get_context_data(self, **kwargs):
        context = super(DomainSongDetail, self).get_context_data(**kwargs)

        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL+'/api/domain_song/'+context['id'])
        if response.status_code == status.HTTP_200_OK:
            context['domain_song'] = response.json
            context['form'] = DomainSongForm()
        return context
