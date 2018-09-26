from rest_framework import viewsets
from telemeta.models.location import Location as LocationModel
from ..serializers.location import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    Location management
    """

    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer
