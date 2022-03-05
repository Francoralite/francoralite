# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.utils.http import urlencode

from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.tools import request_api


class SearchAdvancedView(FrancoraliteTemplateView):
    template_name = "../templates/search_advanced.html"

    def get(self, request, *args, **kwargs):
        url = '/advancedsearch/?' + urlencode(request.GET, doseq=True)
        results = request_api(url)

        context = self.get_context_data(**kwargs)
        context['collections'] = tuple(result for result in results
            if result.get('entity') == 'Collection')
        context['items'] = tuple(result for result in results
            if result.get('entity') == 'Item')
        context['locations'] = tuple(result for result in results
            if result.get('entity') == 'CollectionLocation')

        return self.render_to_response(context)
