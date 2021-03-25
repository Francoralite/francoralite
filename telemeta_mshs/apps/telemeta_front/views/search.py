# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_mshs.apps.telemeta_front.tools as tools
from django.utils.translation import gettext_lazy as _


class SearchView(FrancoraliteTemplateView):
    template_name = "../templates/search.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(SearchView, self).get_context_data(**kwargs)
            query = self.request.GET['q']
            context['query'] = query
            context['results'] = tools.request_api(
                '/globalsearch/?q=' + query)
            context['topics'] = {
                "Authority": _(u"Personnes"),
                "Location": _(u"Lieux"),
                "Fond": _(u"Fonds"),
                "Mission": _(u"Mission"),
                "Collection": _(u"Enquête"),
                "Item": _(u"Item")
            }
        except Exception as err:
            context['results'] = []
            context['error'] = err.message
        return context
