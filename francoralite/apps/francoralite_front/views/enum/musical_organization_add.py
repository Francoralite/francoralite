# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.musical_organization import MusicalOrganizationForm
import francoralite.apps.francoralite_front.tools as tools


class MusicalOrganizationAdd(FormView):
    template_name = "../templates/enum/musical_organization-add.html"
    form_class = MusicalOrganizationForm
    success_url = '/musical_organization/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'musical_organization',
            MusicalOrganizationForm, request, *args, **kwargs)
