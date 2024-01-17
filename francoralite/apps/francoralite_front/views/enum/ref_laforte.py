# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from francoralite.apps.francoralite_front.francoralite_template_view import (
    FrancoraliteTemplateView,
)
import francoralite.apps.francoralite_front.tools as tools

class RefLaforteView(FrancoraliteTemplateView):
    template_name = "../templates/enum/ref_laforte.html"

    keycloak_scopes = {"GET": "ref_laforte:view"}

    def get_context_data(self, **kwargs):
        try:
            context = super(FrancoraliteTemplateView, self).get_context_data(**kwargs)
            context["ref_lafortes"] = tools.request_api("/api/ref_laforte")
        except Exception as err:
            context["ref_lafortes"] = []
            context["error"] = err
        return context
