# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from ...francoralite_template_view import FrancoraliteFormView
from ...forms.publisher import PublisherForm


class PublisherEdit(FrancoraliteFormView):
    template_name = "../templates/enum/publisher-add.html"
    form_class = PublisherForm
    api_url_prefix = '/api/publisher/'
    entity_name = 'publisher'
    template_variable_name = 'publisher'
    success_url = '/publisher/'
