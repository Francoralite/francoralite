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
        api_response = request_api(url)

        context = self.get_context_data(**kwargs)
        context['collections'] = api_response['results']['collections']
        context['items'] = api_response['results']['items']
        context['locations'] = api_response['results']['locations']

        return self.render_to_response(context)
