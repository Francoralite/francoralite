# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.forms.domain_music import DomainMusicForm
import francoralite.apps.francoralite_front.tools as tools


class DomainMusicDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_music-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainMusicDetail, self).get_context_data(**kwargs)
            context['domain_music'] = tools.request_api(
                '/api/domain_music/' + context['id'])
            context['form'] = DomainMusicForm()

        except Exception as err:
            context['domain_music'] = {}
            context['error'] = err.message
            context['form'] = DomainMusicForm()
        return context
