# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from telemeta_front.forms.location_gis import LocationForm
import telemeta_front.tools as tools


class LocationAdd(FormView):
    template_name = "../templates/location-add.html"
    form_class = LocationForm
    success_url = '/location_gis/'

    def post(self, request, *args, **kwargs):
        return tools.post(
            'location_gis', LocationForm, request, *args, **kwargs)
