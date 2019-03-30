from rest_framework import viewsets, filters
from ..models.location import Location as LocationModel
from ..serializers.location_gis import LocationGisSerializer


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
