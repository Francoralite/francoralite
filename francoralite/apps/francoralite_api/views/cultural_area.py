# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.cultural_area import CulturalArea as CulturalAreaModel
from ..serializers.cultural_area import CulturalAreaSerializer


class CulturalAreaViewSet(viewsets.ModelViewSet):
    """
    CulturalArea management
    """

    queryset = CulturalAreaModel.objects.all()
    serializer_class = CulturalAreaSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'cultural_area:view',
        'POST': 'cultural_area:add',
        'PATCH': 'cultural_area:update',
        'PUT': 'cultural_area:update',
        'DELETE': 'cultural_area:delete',
    }
