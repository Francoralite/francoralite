from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models.block import Block as BlockModel
from ..serializers.block import BlockSerializer


class BlockViewSet(viewsets.ModelViewSet):
    """
    Block management
    """

    queryset = BlockModel.objects.all()
    serializer_class = BlockSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('type', 'show')
    ordering = ('order', 'title')
    search_fields = ('title', 'content')

    keycloak_scopes = {
        'GET': 'block:view',
        'POST': 'block:add',
        'PATCH': 'block:update',
        'PUT': 'block:update',
        'DELETE': 'block:delete',
    }
