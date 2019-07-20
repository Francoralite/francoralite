from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from ..models.location import Location as LocationModel
from ..models.collection_location import (
    CollectionLocation as CollectionLocationModel)
from ..models.item import Item as ItemModel
from ..serializers.location_gis import LocationGisSerializer
from ..serializers.item import ItemSerializer


class LocationGISViewSet(viewsets.ModelViewSet):
    """
    Location GIS management
    """

    queryset = LocationModel.objects.all()
    serializer_class = LocationGisSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ()
    ordering = ('name',)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'location_gis:view',
        'POST': 'location_gis:add',
        'PATCH': 'location_gis:update',
        'PUT': 'location_gis:update',
        'DELETE': 'location_gis:delete'
    }

    @detail_route()
    def items(self, request, pk=None):
        instance = self.get_object()

        # Retrieve the collections, related to the current location
        list_collection = CollectionLocationModel.objects.filter(
                 location_id=instance.id).values_list(
                     'collection', flat=True)
        # Retrieve the items, related to each collection
        items = ItemModel.objects.filter(
            collection__in=[str(x) for x in list_collection])
        # Push the items to the data results
        data = [ItemSerializer(i).data for i in items]

        return Response(data)
