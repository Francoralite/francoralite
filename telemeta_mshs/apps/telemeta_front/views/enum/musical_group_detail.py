# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
import telemeta_front.tools as tools
from telemeta_front.forms.musical_group import MusicalGroupForm


class MusicalGroupDetail(TemplateView):
    template_name = "../templates/enum/musical_group-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(MusicalGroupDetail, self).get_context_data(**kwargs)
            context['musical_group'] = tools.request_api(
                '/api/musical_group/' + context['id'])
            context['form'] = MusicalGroupForm
        except Exception as err:
            context['musical_group'] = {}
            context['error'] = err.message
            context['form'] = MusicalGroupForm
        return context
