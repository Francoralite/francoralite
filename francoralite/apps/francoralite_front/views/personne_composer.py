# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ..francoralite_template_view import FrancoralitePaginatedTemplateView


class PersonneComposerView(FrancoralitePaginatedTemplateView):
    api_url = '/api/authority?is_composer=true&ordering=last_name,first_name'
    context_results_name = 'personnes'
    template_name = '../templates/personne_composer.html'
    keycloak_scopes = {
        'GET': 'authority:view',
    }
