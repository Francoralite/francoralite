# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ...francoralite_template_view import FrancoraliteFormView
from ...forms.domain_vocal import DomainVocalForm


class DomainVocalEdit(FrancoraliteFormView):
    template_name = "../templates/enum/domain_vocal-add.html"
    api_url_prefix = '/api/domain_vocal/'
    entity_name = 'domain_vocal'
    form_class = DomainVocalForm
    template_variable_name = 'domain_vocal'
    success_url = '/domain_vocal/'

    keycloak_scopes = {
        'DEFAULT': 'domain_vocal:update',
    }
