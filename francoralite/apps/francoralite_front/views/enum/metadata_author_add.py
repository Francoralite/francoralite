# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.metadata_author import MetadataAuthorForm
import francoralite.apps.francoralite_front.tools as tools


class MetadataAuthorAdd(FormView):
    template_name = "../templates/enum/metadata_author-add.html"
    form_class = MetadataAuthorForm
    success_url = '/metadata_author/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'metadata_author', MetadataAuthorForm, request, *args, **kwargs)
