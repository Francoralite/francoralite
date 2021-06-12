# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView


class SearchAdvancedView(FrancoraliteTemplateView):
    template_name = "../templates/search_advanced.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(
                SearchAdvancedView, self).get_context_data(**kwargs)
            context["collections"] = []

        except Exception as err:
            context["collections"] = []
            context['error'] = err.message
        return context
