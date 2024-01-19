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
        if request.GET:
            url = '/advancedsearch/?' + urlencode(request.GET, doseq=True)
            api_response = request_api(url)
        else:
            api_response = {}

        context = self.get_context_data(**kwargs)
        context['show_results'] = bool(api_response)
        context['search_warning'] = api_response.get('warning', {})
        context['pagination'] = api_response.get('pagination', {})

        context['records'] = api_response.get('results', {}).get('records', ())
        context['locations'] = api_response.get('results', {}).get('locations', ())

        context['parameters'] = api_response.get('parameters', {})
        context['parameters_instances_json'] = dict(
            (name, json.dumps(values))
            for name, values in api_response.get('parameters', {}).get('instances', {}).items()
        )

        return self.render_to_response(context)
