# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.ref_laforte import RefLaforteForm
from ... import tools as tools


class RefLaforteDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/ref_laforte-detail.html"

    keycloak_scopes = {
        "DEFAULT": "ref_laforte:view",
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(RefLaforteDetail, self).get_context_data(**kwargs)
            context["ref_laforte"] = tools.request_api("/api/ref_laforte/" + context["id"])
            context["form"] = RefLaforteForm()
        except Http404:
            raise Http404(_("Cette référence Laforte n’existe pas."))
        except Exception as err:
            context["ref_laforte"] = {}
            context["error"] = err
            context["form"] = RefLaforteForm()
        return context
