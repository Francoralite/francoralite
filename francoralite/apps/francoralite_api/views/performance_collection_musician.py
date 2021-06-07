# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
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

    keycloak_scopes = {
        'GET': 'performance_collection_musician:view',
        'POST': 'performance_collection_musician:add',
        'PATCH': 'performance_collection_musician:update',
        'PUT': 'performance_collection_musician:update',
        'DELETE': 'performance_collection_musician:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = PerformanceCollectionMusicianModel.objects.filter(
                performance_collection_id=self.kwargs['performance_pk']
                )
        return queryset
