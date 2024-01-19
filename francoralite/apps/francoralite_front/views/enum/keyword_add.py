# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.keyword import KeywordForm
from ... import tools as tools


class KeywordAdd(FormView):
    template_name = "../templates/enum/keyword-add.html"
    form_class = KeywordForm
    success_url = '/keyword/'

    keycloak_scopes = {
        'DEFAULT': 'keyword:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('keyword', KeywordForm, request, *args, **kwargs)
