# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_performance import (
    ItemPerformance as ItemPerformanceModel)
from ..serializers.item_performance import (
    ItemPerformanceSerializer)


class ItemPerformanceViewSet(viewsets.ModelViewSet):
    """
    ItemPerformance management
    """

    queryset = ItemPerformanceModel.objects.all()
    serializer_class = ItemPerformanceSerializer

    keycloak_scopes = {
        'GET': 'item_performance:view',
        'POST': 'item_performance:add',
        'PATCH': 'item_performance:update',
        'PUT': 'item_performance:update',
        'DELETE': 'item_performance:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemPerformanceModel.objects.filter(
                item_id=self.kwargs['item_pk'])
        return queryset
