# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from telemeta_front.forms.domain_tale import DomainTaleForm
import telemeta_front.tools as tools


class DomainTaleAdd(FormView):
    template_name = "../templates/enum/domain_tale-add.html"
    form_class = DomainTaleForm
    success_url = '/domain_tale/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'domain_tale', DomainTaleForm, request, *args, **kwargs)
