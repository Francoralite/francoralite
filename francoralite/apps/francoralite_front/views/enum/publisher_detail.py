# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.forms.publisher import PublisherForm
import francoralite.apps.francoralite_front.tools as tools


class PublisherDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/publisher-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(PublisherDetail, self).get_context_data(**kwargs)
            context['publisher'] = tools.request_api(
                '/api/publisher/' + context['id'])
            context['form'] = PublisherForm()

        except Exception as err:
            context['publisher'] = {}
            context['error'] = err
            context['form'] = PublisherForm()
        return context
