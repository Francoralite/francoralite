# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools
from francoralite.apps.francoralite_front.forms.personne import PersonneForm


class PersonneDetail(FrancoraliteTemplateView):
    template_name = "../templates/personne-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(PersonneDetail, self).get_context_data(**kwargs)
            # Obtain values of the record authority
            context['personne'] = tools.request_api(
                '/api/authority/' + context['id'])
            context['contribs'] = tools.request_api(
                '/api/authority/' + context['id'] + '/contribs')
            context['form'] = PersonneForm
        except Exception as err:
            context['personne'] = {}
            context['contribs'] = {}
            context['error'] = err
        return context
