# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.domain_music import DomainMusicForm


class DomainMusicEdit(FrancoraliteFormView):
    api_url_prefix = '/api/domain_music/'
    entity_name = 'domain_music'
    template_name = "../templates/enum/domain_music-add.html"
    form_class = DomainMusicForm
    template_variable_name = 'domain_music'
    success_url = '/domain_music/'

 
    keycloak_scopes = {
        'DEFAULT': 'domain_music:update',
    }