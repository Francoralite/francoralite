# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from telemeta_mshs.apps.telemeta_front.forms.thematic import ThematicForm
import telemeta_mshs.apps.telemeta_front.tools as tools


class ThematicDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/thematic-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(ThematicDetail, self).get_context_data(**kwargs)
            context['thematic'] = tools.request_api(
                '/api/thematic/' + context['id'])
            context['form'] = ThematicForm()

        except Exception as err:
            context['thematic'] = {}
            context['error'] = err.message
            context['form'] = ThematicForm()
        return context
