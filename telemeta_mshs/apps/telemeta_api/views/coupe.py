from rest_framework import viewsets
from ..models.coupe import Coupe as CoupeModel
from ..serializers.coupe import CoupeSerializer


class CoupeViewSet(viewsets.ModelViewSet):
    """
    Coupe management
    """

    queryset = CoupeModel.objects.all()
    serializer_class = CoupeSerializer
