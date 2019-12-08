# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from telemeta_front.forms.fond import FondForm
import telemeta_front.tools as tools


class FondAdd(FormView):
    template_name = "../templates/fond-add.html"
    form_class = FondForm
    success_url = '/fond/'

    def get_initial(self):
        initial = super(FondAdd, self).get_initial()
        initial['institution'] = self.kwargs['id_institution']

        return initial

    def post(self, request, *args, **kwargs):
        return tools.post('fond', FondForm, request, *args, **kwargs)
