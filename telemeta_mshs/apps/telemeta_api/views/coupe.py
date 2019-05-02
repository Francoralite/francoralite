from rest_framework import viewsets
from ..models.coupe import Coupe as CoupeModel
from ..serializers.coupe import CoupeSerializer


class CoupeViewSet(viewsets.ModelViewSet):
    """
    Coupe management
    """

    queryset = CoupeModel.objects.all()
    serializer_class = CoupeSerializer

    keycloak_scopes = {
        'GET': 'coupe:view',
        'POST': 'coupe:add',
        'PATCH': 'coupe:update',
        'PUT': 'coupe:update',
        'DELETE': 'coupe:delete'
    }
