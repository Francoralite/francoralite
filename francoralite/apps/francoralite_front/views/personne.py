# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from .. import tools
from ..forms.personne import PersonneForm
from ..francoralite_template_view import FrancoraliteTemplateView


class PersonneView(FrancoraliteTemplateView):
    template_name = '../templates/personne.html'
    keycloak_scopes = {
        'GET': 'authority:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(PersonneView, self).get_context_data(**kwargs)
            context['personnes'] = tools.request_api('/api/authority?ordering=last_name,first_name')
            context['form'] = PersonneForm
        except Exception as err:
            context['personnes'] = []
            context['error'] = err
        return context
