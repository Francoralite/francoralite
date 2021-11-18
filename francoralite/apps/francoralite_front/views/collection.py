# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from .. import tools
from ..forms.collection import CollectionForm
from ..francoralite_template_view import FrancoraliteTemplateView


class CollectionView(FrancoraliteTemplateView):
    template_name = '../templates/collection.html'
    keycloak_scopes = {
        'GET': 'collection:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(CollectionView, self).get_context_data(**kwargs)
            context['collections'] = tools.request_api('/api/collection')
            context['form'] = CollectionForm
        except Exception as err:
            context['collections'] = []
            context['error'] = err
        return context
