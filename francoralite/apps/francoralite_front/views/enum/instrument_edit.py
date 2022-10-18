# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.instrument import InstrumentForm



class InstrumentEdit(FrancoraliteFormView):
    template_name = "../templates/enum/instrument-add.html"
    api_url_prefix = '/api/instrument/'
    entity_name = 'instrument'
    form_class = InstrumentForm
    template_variable_name = 'instrument'
    success_url = '/instrument/'

    keycloak_scopes = {
        'DEFAULT': 'instrument:update',
    }
