# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.mediatype import MediaTypeForm
from ... import tools as tools


class MediaTypeAdd(FormView):
    template_name = "../templates/enum/mediatype-add.html"
    form_class = MediaTypeForm
    success_url = '/mediatype/'
    
    keycloak_scopes = {
        'DEFAULT': 'mediatype:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('mediatype', MediaTypeForm, request, *args, **kwargs)
