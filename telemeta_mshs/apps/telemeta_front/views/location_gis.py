# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_mshs.apps.telemeta_front.tools as tools


class LocationView(FrancoraliteTemplateView):
    template_name = "../templates/location.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(LocationView, self).get_context_data(**kwargs)
            context['locations'] = tools.request_api('/api/locationgis')
        except Exception as err:
            context['locations'] = []
            context['error'] = err.message
        return context
