# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class DomainSongView(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_song.html"

    keycloak_scopes = {'GET': 'domain_song:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainSongView, self).get_context_data(**kwargs)
            context['domain_songs'] = tools.request_api('/api/domain_song/')
        except Exception as err:
            context['domain_songs']
            context['error'] = err.message

        return context
