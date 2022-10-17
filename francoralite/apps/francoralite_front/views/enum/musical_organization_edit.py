# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.musical_organization import MusicalOrganizationForm


class MusicalOrganizationEdit(FrancoraliteFormView):
    template_name = "../templates/enum/musical_organization-add.html"
    form_class = MusicalOrganizationForm
    api_url_prefix = '/api/musical_organization/'
    entity_name = 'musical_organization'
    template_variable_name = 'musical_organization'
    success_url = '/musical_organization/'

    keycloak_scopes = {
        'DEFAULT': 'musical_organization:update',
    }
