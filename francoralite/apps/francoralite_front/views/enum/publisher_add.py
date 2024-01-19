# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from ...forms.publisher import PublisherForm
from ... import tools as tools


class PublisherAdd(FormView):
    template_name = "../templates/enum/publisher-add.html"
    form_class = PublisherForm
    success_url = '/publisher/'
    
    keycloak_scopes = {
        'DEFAULT': 'publisher:add',
    }

    def post(self, request, *args, **kwargs):
        return tools.post('publisher', PublisherForm, request, *args, **kwargs)
