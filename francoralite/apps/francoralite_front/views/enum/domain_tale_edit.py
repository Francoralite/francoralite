# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.domain_tale import DomainTaleForm


class DomainTaleEdit(FrancoraliteFormView):
    template_name = "../templates/enum/domain_tale-add.html"
    api_url_prefix = '/api/domain_tale/'
    entity_name = 'domain_tale'
    form_class = DomainTaleForm
    template_variable_name = 'domain_tale'
    success_url = '/domain_tale/'

    keycloak_scopes = {
        'DEFAULT': 'domain_tale:update',
    }
