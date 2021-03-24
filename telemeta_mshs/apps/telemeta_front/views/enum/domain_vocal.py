# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_mshs.apps.telemeta_front.tools as tools


class DomainVocalView(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_vocal.html"

    keycloak_scopes = {'GET': 'domain_vocal:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainVocalView, self).get_context_data(**kwargs)
            context['domain_vocals'] = tools.request_api('/api/domain_vocal')
        except Exception as err:
            context['domain_vocals'] = []
            context['error'] = err.message

        return context
