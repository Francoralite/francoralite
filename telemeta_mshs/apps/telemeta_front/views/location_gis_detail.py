# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools

from telemeta_front.forms.location_gis import LocationForm


class LocationDetail(FrancoraliteTemplateView):
    template_name = "../templates/location-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(LocationDetail, self).get_context_data(**kwargs)
            # Obtain values of the record location
            context['location'] = tools.request_api(
                '/api/locationgis/' + context['id'])
            context['form'] = LocationForm
        except Exception as err:
            context['institution'] = {}
            context['error'] = err.message
        return context
