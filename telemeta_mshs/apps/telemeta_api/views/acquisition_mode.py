from rest_framework import viewsets
from ..models.acquisition_mode import AcquisitionMode as AcquisitionModel
from ..serializers.acquisition_mode import AcquisitionModeSerializer


class AcquisitionModeViewSet(viewsets.ModelViewSet):
    """
    Coupe management
    """

    queryset = AcquisitionModel.objects.all()
    serializer_class = AcquisitionModeSerializer
