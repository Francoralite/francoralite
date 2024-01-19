# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..francoralite_template_view import FrancoralitePaginatedTemplateView


class InstitutionView(FrancoralitePaginatedTemplateView):
    api_url = '/api/institution'
    context_results_name = 'institutions'
    template_name = '../templates/institution.html'
    keycloak_scopes = {
        'GET': 'institution:view',
    }
