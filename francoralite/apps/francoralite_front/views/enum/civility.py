# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools


class CivilityView(FrancoraliteTemplateView):
    template_name = "../templates/enum/civility.html"

    keycloak_scopes = {'GET': 'civility:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(CivilityView, self).get_context_data(**kwargs)
            context['civilities'] = tools.request_api('/api/civility')
        except Exception as err:
            context['civilities'] = []
            context['error'] = err

        return context
