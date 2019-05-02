# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from telemeta_front.forms.mediatype import MediaTypeForm
import telemeta_front.tools as tools


class MediaTypeDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/mediatype-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(MediaTypeDetail, self).get_context_data(**kwargs)
            context['mediatype'] = tools.request_api(
                '/api/mediatype/' + context['id'])
            context['form'] = MediaTypeForm()

        except Exception as err:
            context['mediatype'] = {}
            context['error'] = err.message
            context['form'] = MediaTypeForm()
        return context
