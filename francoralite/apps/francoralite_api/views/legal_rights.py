from rest_framework import viewsets
from ..models.legal_rights import LegalRights as LegalRightsModel
from ..serializers.legal_rights import LegalRightsSerializer


class LegalRightsViewSet(viewsets.ModelViewSet):
    """
    LegalRights management
    """

    queryset = LegalRightsModel.objects.all()
    serializer_class = LegalRightsSerializer

    keycloak_scopes = {
        'GET': 'legal_rights:view',
        'POST': 'legal_rights:add',
        'PATCH': 'legal_rights:update',
        'PUT': 'legal_rights:update',
        'DELETE': 'legal_rights:delete'
    }
