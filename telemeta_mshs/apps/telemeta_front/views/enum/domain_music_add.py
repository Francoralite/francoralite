# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from telemeta_mshs.apps.telemeta_front.forms.domain_music import DomainMusicForm
import telemeta_mshs.apps.telemeta_front.tools as tools


class DomainMusicAdd(FormView):
    template_name = "../templates/enum/domain_music-add.html"
    form_class = DomainMusicForm
    success_url = '/domain_music/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'domain_music', DomainMusicForm, request, *args, **kwargs)
