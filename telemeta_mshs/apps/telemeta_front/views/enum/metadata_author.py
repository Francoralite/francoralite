# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class MetadataAuthorView(FrancoraliteTemplateView):
    template_name = "../templates/enum/metadata_author.html"

    keycloak_scopes = {'GET': 'metadata_author:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(MetadataAuthorView, self).get_context_data(**kwargs)
            context['metadata_author'] = tools.request_api('/api/legalrights/')
        except Exception as err:
            context['metadata_author'] = []
            context['error'] = err.message

        return context
