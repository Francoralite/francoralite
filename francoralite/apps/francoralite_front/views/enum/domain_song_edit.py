# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.domain_song import DomainSongForm


class DomainSongEdit(FrancoraliteFormView):
    api_url_prefix = '/api/domain_song/'
    entity_name = 'domain_song'
    template_name = "../templates/enum/domain_song-add.html"
    form_class = DomainSongForm
    template_variable_name = 'domain_song'
    success_url = '/domain_song/'
