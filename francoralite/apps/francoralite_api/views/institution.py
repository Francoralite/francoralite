from rest_framework import viewsets, filters
from ..models.institution import Institution as InstitutionModel
from ..serializers.institution import InstitutionSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    Institution management
    """

    queryset = InstitutionModel.objects.all()
    serializer_class = InstitutionSerializer

    filter_backends = (filters.OrderingFilter,)
    ordering = ('name',)

    keycloak_scopes = {
        'GET': 'institution:view',
        'POST': 'institution:add',
        'PATCH': 'institution:update',
        'PUT': 'institution:update',
        'DELETE': 'institution:delete'
    }
