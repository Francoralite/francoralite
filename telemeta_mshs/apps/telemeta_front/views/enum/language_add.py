# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from telemeta_mshs.apps.telemeta_front.forms.language import LanguageForm
import telemeta_mshs.apps.telemeta_front.tools as tools


class LanguageAdd(FormView):
    template_name = "../templates/enum/language-add.html"
    form_class = LanguageForm
    success_url = '/language/'

    def post(self, request, *args, **kwargs):
        return tools.post('language', LanguageForm, request, *args, **kwargs)
