# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_performance_collection import (
    ItemPerformanceCollection as ItemPerformanceCollectionModel)
from ..serializers.item_performance_collection import (
    ItemPerformanceCollectionSerializer)


class ItemPerformanceCollectionViewSet(viewsets.ModelViewSet):
    """
    ItemPerformanceCollection management
    """

    queryset = ItemPerformanceCollectionModel.objects.all()
    serializer_class = ItemPerformanceCollectionSerializer

    keycloak_scopes = {
        'GET': 'item_performance_collection:view',
        'POST': 'item_performance_collection:add',
        'PATCH': 'item_performance_collection:update',
        'PUT': 'item_performance_collection:update',
        'DELETE': 'item_performance_collection:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemPerformanceCollectionModel.objects.filter(
                item_id=self.kwargs['item_pk'])
        return queryset
