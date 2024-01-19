# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..francoralite_template_view import FrancoralitePaginatedTemplateView
from ..widgets import DomainsBarLoader


class FondView(FrancoralitePaginatedTemplateView):
    api_url = '/api/fond'
    complementary_data_loaders = (
        DomainsBarLoader(api_url + '/{id}/items_domains'),
    )
    context_results_name = 'fonds'
    template_name = '../templates/fond.html'
    keycloak_scopes = {
        'GET': 'fond:view',
    }
