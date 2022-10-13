# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
from francoralite.apps.francoralite_front.forms.block import BlockForm
import francoralite.apps.francoralite_front.tools as tools


class BlockView(FrancoraliteTemplateView):
    template_name = "../templates/enum/block.html"

    keycloak_scopes = {'GET': 'block:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(BlockView, self).get_context_data(**kwargs)
            context['blocks'] = tools.request_api('/api/block')

            type_labels = dict(BlockForm.TYPE_CHOICES)
            for block in context['blocks']:
                block['type_label'] = type_labels.get(block['type'])
        except Exception as err:
            context['blocks'] = []
            context['error'] = err

        return context
