# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools


class DomainMusicView(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_music.html"

    keycloak_scopes = {'GET': 'domain_music:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainMusicView, self).get_context_data(**kwargs)
            context['domain_musics'] = tools.request_api('/api/domain_music')
        except Exception as err:
            context['domain_musics'] = []
            context['error'] = err

        return context
