# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from telemeta_mshs.apps.telemeta_front.forms.domain_song import DomainSongForm
import telemeta_mshs.apps.telemeta_front.tools as tools


class DomainSongAdd(FormView):
    template_name = "../templates/enum/domain_song-add.html"
    form_class = DomainSongForm
    success_url = '/domain_song/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'domain_song', DomainSongForm, request, *args, **kwargs)
