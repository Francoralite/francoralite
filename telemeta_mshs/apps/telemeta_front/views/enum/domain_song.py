# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
import requests
from settings import FRONT_HOST_URL
from telemeta_front.forms.domain_song import DomainSongForm


class DomainSongView(TemplateView):
    template_name = "../templates/enum/domain_song.html"

    def get_context_data(self, **kwargs):
        context = super(DomainSongView, self).get_context_data(**kwargs)
        context['domain_songs'] = requests.get(
            FRONT_HOST_URL + '/api/domain_song/').json
        context['form'] = DomainSongForm
        return context
