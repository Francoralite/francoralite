# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from ..models.mission import Mission as MissionModel
from ..models.collection import Collection as CollectionModel
from ..models.collection_informer import (
    CollectionInformer as CollectionInformerModel)
from ..models.authority import Authority as AuthorityModel
from ..serializers.mission import MissionSerializer
from ..serializers.authority import AuthoritySerializer


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

    @detail_route()
    def informers(self, request, pk=None):
        instance = self.get_object()

        # Retrieve the collections, related to the current mission
        collections = CollectionModel.objects.filter(
            mission_id=instance.id).values_list(
                'id', flat=True)
        # Retrieve the informers, related to the collections
        list_informers = CollectionInformerModel.objects.filter(
                 collection_id__in=[str(x) for x in collections]
                 ).values_list(
                     'informer', flat=True)

        # Retrieve the informer
        informers = AuthorityModel.objects.filter(
            id__in=[str(x) for x in list_informers])

        # Push the informers to the data results
        data = [AuthoritySerializer(i).data for i in informers]

        return Response(data)
