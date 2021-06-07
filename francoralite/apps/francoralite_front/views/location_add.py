# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from francoralite.apps.francoralite_front.forms.location import LocationForm
import francoralite.apps.francoralite_front.tools as tools


class LocationAdd(FormView):
    template_name = "../templates/location-add.html"
    form_class = LocationForm
    success_url = '/location/'

    def post(self, request, *args, **kwargs):
        return tools.post('location', LocationForm, request, *args, **kwargs)
