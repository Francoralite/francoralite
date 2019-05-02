# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from telemeta_front.forms.metadata_author import MetadataAuthorForm
import telemeta_front.tools as tools


class MetadataAuthorDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/metadata_author-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(MetadataAuthorDetail, self).get_context_data(**kwargs)
            context['metadata_author'] = tools.request_api(
                '/api/legalrights/' + context['id'])
            context['form'] = MetadataAuthorForm()

        except Exception as err:
            context['metadata_author'] = {}
            context['error'] = err.message
            context['form'] = MetadataAuthorForm()
        return context
