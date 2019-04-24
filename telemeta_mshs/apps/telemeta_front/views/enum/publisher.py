# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class PublisherView(FrancoraliteTemplateView):
    template_name = "../templates/enum/publisher.html"

    keycloak_scopes = {'GET': 'publisher:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(PublisherView, self).get_context_data(**kwargs)
            context['publishers'] = tools.request_api('/api/publisher/')
        except Exception as err:
            context['publishers'] = []
            context['error'] = err.message

        return context
