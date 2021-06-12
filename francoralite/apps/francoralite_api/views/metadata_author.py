from rest_framework import viewsets
from ..models.metadata_author import MetadataAuthor as MetadataAuthorModel
from ..serializers.metadata_author import MetadataSerializer


class MetadataAuthorViewSet(viewsets.ModelViewSet):
    """
    MetadataAuthor management
    """

    queryset = MetadataAuthorModel.objects.all()
    serializer_class = MetadataSerializer

    keycloak_scopes = {
        'GET': 'metadata_author:view',
        'POST': 'metadata_author:add',
        'PATCH': 'metadata_author:update',
        'PUT': 'metadata_author:update',
        'DELETE': 'metadata_author:delete'
    }
