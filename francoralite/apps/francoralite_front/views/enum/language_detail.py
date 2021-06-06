# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools
from francoralite.apps.francoralite_front.forms.language import LanguageForm


class LanguageDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/language-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(LanguageDetail, self).get_context_data(**kwargs)
            context['language'] = tools.request_api(
                '/api/language/' + context['id'])
            context['form'] = LanguageForm()
        except Exception as err:
            context['language'] = {}
            context['error'] = err.message
            context['form'] = LanguageForm()
        return context
