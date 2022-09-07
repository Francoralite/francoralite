# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..francoralite_template_view import FrancoralitePaginatedTemplateView
from ..widgets import DefaultLoader, DomainsBarLoader


class MissionView(FrancoralitePaginatedTemplateView):
    api_url = '/api/mission'
    complementary_data_loaders = (
        DefaultLoader(api_url + '/{id}/subelements_count', 'subelements_count'),
        DomainsBarLoader(api_url + '/{id}/items_domains'),
    )
    context_results_name = 'missions'
    template_name = '../templates/mission.html'
    keycloak_scopes = {
        'GET': 'mission:view',
    }
