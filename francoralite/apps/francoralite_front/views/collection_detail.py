# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ..francoralite_template_view import FrancoraliteTemplateView
import francoralite_front.tools as tools
from ..forms.collection import CollectionForm


class CollectionDetail(FrancoraliteTemplateView):
    template_name = "../templates/collection-detail.html"
    
    keycloak_scopes = {
        'DEFAULT': 'collection:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(CollectionDetail, self).get_context_data(**kwargs)
            # Obtain values of the record collection
            context['collection'] = tools.request_api(
              '/api/collection/'+context['id']+'/complete')
            # Obtain values of related items
            context['items'] = tools.request_api(
                '/api/item?collection=' + context['id'])
            context['form'] = CollectionForm()
            # Obtain values of related documents
            context['documents'] = tools.request_api(
                '/api/collection/' + context['id'] + '/document')
        except Http404:
            raise Http404(_('Cette enquête n’existe pas.'))
        except Exception as err:
            context['collection'] = {}
            context['items'] = []
            context['documents'] = []
            context['error'] = str(err) + ":" + str(type(err).__name__)
        return context
