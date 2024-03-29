# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..francoralite_template_view import FrancoralitePaginatedTemplateView


class ItemView(FrancoralitePaginatedTemplateView):
    api_url = '/api/item'
    context_results_name = 'items'
    template_name = '../templates/item.html'
    keycloak_scopes = {
        'GET': 'item:view',
    }
