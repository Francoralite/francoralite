# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import viewsets, filters
from ..models.performance_collection import (
    PerformanceCollection as PerformanceCollectionModel)
from ..serializers.performance_collection import (
    PerformanceCollectionSerializer)


class PerformanceCollectionViewSet(viewsets.ModelViewSet):
    """
    PerformanceCollection management
    """

    queryset = PerformanceCollectionModel.objects.all()
    serializer_class = PerformanceCollectionSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('collection', 'instrument')
    ordering = ('collection', 'instrument', 'number')
    search_fields = ('number')

    keycloak_scopes = {
        'GET': 'performance_collection:view',
        'POST': 'performance_collection:add',
        'PATCH': 'performance_collection:update',
        'PUT': 'performance_collection:update',
        'DELETE': 'performance_collection:delete'
    }
