# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import generics

from ..models.collection import Collection
from ..models.fond import Fond
from ..models.item import Item
from ..models.mission import Mission
from ..serializers.core import SimpleSerializer


class CodeInternalView(generics.ListAPIView):
    serializer_class = SimpleSerializer

    keycloak_scopes = {
        'GET': 'item:view',
    }

    def get_queryset(self):
        search = self.request.query_params.get('search', None)

        models = (Fond, Mission, Collection, Item)

        querysets = tuple(
            model.objects.values_list('code', flat=True).exclude(code=None).exclude(code='')
            for model in models
        )

        if search:
            querysets = tuple(qs.filter(code__istartswith=search) for qs in querysets)

        return querysets[0].union(*querysets[1:]).order_by('code').distinct()