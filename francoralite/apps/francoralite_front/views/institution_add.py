# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.institution import InstitutionForm
import francoralite.apps.francoralite_front.tools as tools


class InstitutionAdd(FormView):
    template_name = "../templates/institution-add.html"
    form_class = InstitutionForm
    success_url = '/institution/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'institution', InstitutionForm, request, *args, **kwargs)
