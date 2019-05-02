# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from ..models.hornbostelsachs import HornbostelSachs as HornbostelSachsModel
from ..serializers.hornbostelsachs import HornbostelSachsSerializer


class HornbostelSachsViewSet(viewsets.ModelViewSet):
    """
    HornbostelSachs management
    """

    queryset = HornbostelSachsModel.objects.all()
    serializer_class = HornbostelSachsSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('number',)
    ordering = ('number', 'name',)
    search_fields = ('number', 'name')

    keycloak_scopes = {
        'GET': 'hornbostelsachs:view',
        'POST': 'hornbostelsachs:add',
        'PATCH': 'hornbostelsachs:update',
        'PUT': 'hornbostelsachs:update',
        'DELETE': 'hornbostelsachs:delete'
    }
