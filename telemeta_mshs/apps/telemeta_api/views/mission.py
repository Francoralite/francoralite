# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from ..models.mission import Mission as MissionModel
from ..serializers.mission import MissionSerializer


class MissionViewSet(viewsets.ModelViewSet):
    """
    Mission management
    """

    queryset = MissionModel.objects.all()
    serializer_class = MissionSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('fonds',)
    ordering = ('fonds', 'code',)
    search_fields = ('fonds', 'code', 'title')

    keycloak_scopes = {
        'GET': 'mission:view',
        'POST': 'mission:add',
        'PATCH': 'mission:update',
        'PUT': 'mission:update',
        'DELETE': 'mission:delete'
    }
