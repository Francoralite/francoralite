# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.ref_laforte import RefLaforteForm


class RefLaforteEdit(FrancoraliteFormView):
    template_name = "../templates/enum/ref_laforte-add.html"
    form_class = RefLaforteForm
    api_url_prefix = "/api/ref_laforte/"
    entity_name = "ref_laforte"
    template_variable_name = "ref_laforte"
    success_url = "/ref_laforte/"

    keycloak_scopes = {
        "DEFAULT": "ref_laforte:update",
    }
