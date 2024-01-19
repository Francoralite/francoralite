# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.domain_music import DomainMusicForm
from ... import tools as tools


class DomainMusicAdd(FormView):
    template_name = "../templates/enum/domain_music-add.html"
    form_class = DomainMusicForm
    success_url = '/domain_music/'
    
    keycloak_scopes = {
        'DEFAULT': 'domain_music:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post(
            'domain_music', DomainMusicForm, request, *args, **kwargs)
