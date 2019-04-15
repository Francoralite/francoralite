# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
from telemeta_front.forms.domain_song import DomainSongForm
import telemeta_front.tools as tools


class DomainSongDetail(TemplateView):
    template_name = "../templates/enum/domain_song-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainSongDetail, self).get_context_data(**kwargs)
            context['domain_song'] = tools.request_api(
                '/api/domain_song/' + context['id'])
            context['form'] = DomainSongForm()

        except Exception as err:
            context['domain_song'] = {}
            context['error'] = err.message
            context['form'] = DomainSongForm()
        return context
