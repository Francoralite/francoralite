# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from ..models.performance import Performance as PerformanceModel
from ..serializers.performance import PerformanceSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    """
    Performance management
    """

    queryset = PerformanceModel.objects.all()
    serializer_class = PerformanceSerializer

    filter_backends = (DjangoFilterBackend,
                        filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('instrument', 'emit')
    ordering = ('instrument', 'emit')
    search_fields = ('instrument', 'emit')

    keycloak_scopes = {
        'GET': 'performance:view',
        'POST': 'performance:add',
        'PATCH': 'performance:update',
        'PUT': 'performance:update',
        'DELETE': 'performance:delete'
    }