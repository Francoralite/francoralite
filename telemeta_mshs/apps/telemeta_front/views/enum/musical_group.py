# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class MusicalGroupView(FrancoraliteTemplateView):
    template_name = "../templates/enum/musical_group.html"

    keycloak_scope = {
        'GET': 'musical_group:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(MusicalGroupView, self).get_context_data(**kwargs)
            context['musical_groups'] = tools.request_api(
                '/api/musical_group')
        except Exception as err:
            context['musical_group'] = []
            context['error'] = err.message

        return context
