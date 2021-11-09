# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from francoralite.apps.francoralite_front.forms.personne import PersonneForm
from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteFormView  #noqa


class PersonneEdit(FrancoraliteFormView):
    api_url_prefix = '/api/authority/'
    entity_name = 'authority'

    form_class = PersonneForm
    template_name = '../templates/personne-add.html'
    template_variable_name = 'personne'

    success_url = '/authority/'

    keycloak_scopes = {
        'DEFAULT': 'authority:update',
    }
