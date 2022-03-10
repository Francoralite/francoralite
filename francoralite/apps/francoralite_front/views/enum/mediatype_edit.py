# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.mediatype import MediaTypeForm


class MediaTypeEdit(FrancoraliteFormView):
    template_name = "../templates/enum/mediatype-add.html"
    api_url_prefix = '/api/mediatype/'
    entity_name = 'mediatype'
    form_class = MediaTypeForm
    template_variable_name = 'mediatype'
    success_url = '/mediatype/'
