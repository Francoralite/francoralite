# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.legal_rights import LegalRightsForm


class LegalRightsEdit(FrancoraliteFormView):
    template_name = "../templates/enum/legal_rights-add.html"
    api_url_prefix = '/api/legalrights/'
    entity_name = 'legal_rights'
    form_class = LegalRightsForm
    template_variable_name = 'legal_rights'
    success_url = '/legal_rights/'
