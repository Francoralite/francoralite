# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from francoralite.apps.francoralite_front import tools
from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView


class HomePageView(FrancoraliteTemplateView):

    template_name = "../templates/home.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(HomePageView, self).get_context_data(**kwargs)
            context['blocks'] = tools.request_api('/api/block?show=true')
        except Exception as err:
            context['blocks'] = []
            context['error'] = err

        return context
