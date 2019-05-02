# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import viewsets, filters
from ..models.performance_collection_musician import (
    PerformanceCollectionMusician as PerformanceCollectionMusicianModel)
from ..serializers.performance_collection_musician import (
    PerformanceCollectionMusicianSerializer)


class PerformanceCollectionMusicianViewSet(viewsets.ModelViewSet):
    """
    PerformanceCollection management
    """

    queryset = PerformanceCollectionMusicianModel.objects.all()
    serializer_class = PerformanceCollectionMusicianSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('performance_collection', 'musician')
    ordering = ('performance_collection', 'musician')
    search_fields = ()

    keycloak_scopes = {
        'GET': 'performance_collection_musician:view',
        'POST': 'performance_collection_musician:add',
        'PATCH': 'performance_collection_musician:update',
        'PUT': 'performance_collection_musician:update',
        'DELETE': 'performance_collection_musician:delete'
    }
