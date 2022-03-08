# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import json

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

        context['or_operators'] = request.GET.getlist('or_operators', [])
        context['parameters_json'] = dict(
            (name, json.dumps(values))
            for name, values in api_response['parameters'].items()
        )

        return self.render_to_response(context)
