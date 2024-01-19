# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.edit import FormView
from ...forms.ref_laforte import RefLaforteForm
from ... import tools as tools


class RefLaforteAdd(FormView):
    form_class = RefLaforteForm
    template_name = "../templates/enum/ref_laforte-add.html"
    success_url = "/ref_laforte/"

    keycloak_scopes = {
        "DEFAULT": "ref_laforte:add",
    }

    def post(self, request, *args, **kwargs):
        return tools.post("ref_laforte", RefLaforteForm, request, *args, **kwargs)
