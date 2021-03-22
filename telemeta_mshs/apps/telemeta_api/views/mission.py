# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.mission import Mission as MissionModel
from ..models.collection import Collection as CollectionModel
from ..models.collection_informer import (
    CollectionInformer as CollectionInformerModel)
from ..models.collectioncollectors import (
    CollectionCollectors as CollectionCollectorModel)
from ..models.collection_location import (
    CollectionLocation as CollectionLocationModel)
from ..models.authority import Authority as AuthorityModel
from ..models.location import Location as LocationModel
from ..serializers.mission import MissionSerializer
from ..serializers.authority import AuthoritySerializer
from ..serializers.location_gis import LocationGisSerializer


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

    def list_collections(self, id_mission, field='id'):
        # Retrieve the collections, related to the current mission
        collections = CollectionModel.objects.filter(
            mission_id=id_mission).values_list(
                field, flat=True)

        return collections

    def related_collections(self,
                            id_mission,
                            model_related,
                            model,
                            entity,
                            serializer=AuthoritySerializer):
        # Retrieve the collections, related to the current mission
        collections = self.list_collections(id_mission=id_mission)
        # Retrieve the entities, related to the collections
        list_related = model_related.objects.filter(
                 collection_id__in=[str(x) for x in collections]
                 ).values_list(
                     entity, flat=True)
        # Retrieve the entity
        entities = model.objects.filter(
            id__in=[str(x) for x in list_related])

        # Push the authorities to the data results
        data = [serializer(i).data for i in entities]

        return data

    @action(detail=True)
    def dates(self, request, pk=None):
        """
        Determine the max and th min dates from
          the related collections of a mission
        """
        instance = self.get_object()

        # Retrieve the collections, related to the current mission

        # Dates (start and end) of list_collections
        from_years = self.list_collections(
            id_mission=instance.id,
            field='recorded_from_year')
        to_years = self.list_collections(
            id_mission=instance.id,
            field='recorded_to_year')

        date_start = ""
        date_end = ""
        # Use the min(early) an max(late)
        if len(from_years) >= 1:
            date_start = min(from_years)
        if len(to_years) >= 1:
            date_end = max(to_years)

        return Response((date_start, date_end))

    @action(detail=True)
    def informers(self, request, pk=None):
        instance = self.get_object()

        data = self.related_collections(
            id_mission=instance.id,
            model_related=CollectionInformerModel,
            model=AuthorityModel,
            entity='informer'
            )
        return Response(data)

    @action(detail=True)
    def collectors(self, request, pk=None):
        instance = self.get_object()
        data = self.related_collections(
            id_mission=instance.id,
            model_related=CollectionCollectorModel,
            model=AuthorityModel,
            entity='collector'
            )

        return Response(data)

    @action(detail=True)
    def locations(self, request, pk=None):
        instance = self.get_object()
        data = self.related_collections(
            id_mission=instance.id,
            model_related=CollectionLocationModel,
            model=LocationModel,
            entity='location',
            serializer=LocationGisSerializer
            )
        return Response(data)
