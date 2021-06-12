# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.legal_rights import LegalRightsForm
import francoralite.apps.francoralite_front.tools as tools


class LegalRightsAdd(FormView):
    template_name = "../templates/enum/legal_rights-add.html"
    form_class = LegalRightsForm
    success_url = '/legal_rights/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'legal_rights', LegalRightsForm, request, *args, **kwargs)
