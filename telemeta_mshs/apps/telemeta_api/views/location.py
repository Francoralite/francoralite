from rest_framework import viewsets, filters
from telemeta.models.location import Location as LocationModel
from ..serializers.location import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    Location management
    """

    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = (
        'name', 'latitude', 'longitude')
    ordering = ('code', 'name',)
    search_fields = ('code', 'name')

    keycloak_scopes = {
        'GET': 'location:view',
        'POST': 'location:add',
        'PATCH': 'location:update',
        'PUT': 'location:update',
        'DELETE': 'location:delete'
    }
