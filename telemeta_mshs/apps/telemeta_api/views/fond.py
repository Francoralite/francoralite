# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.fond import Fond as FondModel
from ..models.mission import Mission as MissionModel
from ..models.collection import Collection as CollectionModel
from ..models.collection_informer import (
    CollectionInformer as CollectionInformerModel)
from ..models.collectioncollectors import (
    CollectionCollectors as CollectionCollectorModel)
from ..models.authority import Authority as AuthorityModel

from ..serializers.fond import FondSerializer
from ..serializers.authority import AuthoritySerializer


class FondViewSet(viewsets.ModelViewSet):
    """
    Fond management
    """

    queryset = FondModel.objects.all()
    serializer_class = FondSerializer

    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('institution',)
    # ordering = ('institution', 'code',)
    # search_fields = ('institution__name', 'code', 'title')
    filter_fields = ('code', 'title')

    keycloak_scopes = {
        'GET': 'fond:view',
        'POST': 'fond:add',
        'PATCH': 'fond:update',
        'PUT': 'fond:update',
        'DELETE': 'fond:delete'
    }


    def list_missions(self, id_fonds, field='id'):

        collection_list = []

        # Retrieve the missions, related to the current fonds
        missions = MissionModel.objects.filter(
            fonds_id=id_fonds)

        # Retrieve the collections, for each mission
        for mission in missions:
            collections = CollectionModel.objects.filter(
                mission_id=mission.id).values_list(
                    field, flat=True)
            for collection in collections:
                collection_list.append(collection)

        return collection_list

    def related_collections(self,
                            id_fonds,
                            model_related,
                            model,
                            entity,
                            serializer=AuthoritySerializer):

        # Retrieve the collections, related to the current fonds
        collections = self.list_missions(id_fonds=id_fonds)

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
          the related missions of a fonds
        """
        instance = self.get_object()

        # Retrieve the collections, related to the current fonds

        # Dates (start and end) of list_missions
        from_years = self.list_missions(
            id_fonds=instance.id,
            field='recorded_from_year')
        to_years = self.list_missions(
            id_fonds=instance.id,
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
            id_fonds=instance.id,
            model_related=CollectionInformerModel,
            model=AuthorityModel,
            entity='informer'
            )
        return Response(data)

    @action(detail=True)
    def collectors(self, request, pk=None):
        instance = self.get_object()
        data = self.related_collections(
            id_fonds=instance.id,
            model_related=CollectionCollectorModel,
            model=AuthorityModel,
            entity='collector'
            )

        return Response(data)
