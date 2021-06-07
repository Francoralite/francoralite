# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.personne import PersonneForm
import francoralite.apps.francoralite_front.tools as tools


class PersonneAdd(FormView):
    template_name = "../templates/personne-add.html"
    form_class = PersonneForm
    success_url = '/authority/'

    def post(self, request, *args, **kwargs):
        return tools.post('authority', PersonneForm, request, *args, **kwargs)
