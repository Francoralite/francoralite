# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from .. import tools
from ..forms.institution import InstitutionForm
from ..francoralite_template_view import FrancoraliteTemplateView


class InstitutionView(FrancoraliteTemplateView):
    template_name = '../templates/institution.html'
    keycloak_scopes = {
        'GET': 'institution:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(InstitutionView, self).get_context_data(**kwargs)
            context['institutions'] = tools.request_api('/api/institution')
            context['form'] = InstitutionForm
        except Exception as err:
            context['institutions'] = []
            context['error'] = err
        return context
