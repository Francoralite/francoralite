from rest_framework import viewsets
from ..models.acquisition_mode import AcquisitionMode as AcquisitionModel
from ..serializers.acquisition_mode import AcquisitionModeSerializer


class AcquisitionModeViewSet(viewsets.ModelViewSet):
    """
    Coupe management
    """

    queryset = AcquisitionModel.objects.all()
    serializer_class = AcquisitionModeSerializer

    keycloak_scopes = {
        'GET': 'acquisition_mode:view',
        'POST': 'acquisition_mode:add',
        'PATCH': 'acquisition_mode:update',
        'PUT': 'acquisition_mode:update',
        'DELETE': 'acquisition_mode:delete'
    }
