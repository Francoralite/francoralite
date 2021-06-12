from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models.authority import Authority as AuthorityModel
from ..serializers.authority import AuthoritySerializer


class AuthorityViewSet(viewsets.ModelViewSet):
    """
    Authority management
    """

    queryset = AuthorityModel.objects.all()
    serializer_class = AuthoritySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = (
        'is_collector', 'is_informer',
        'is_author', 'is_composer', 'is_editor')
    ordering = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name')

    keycloak_scopes = {
        'GET': 'authority:view',
        'POST': 'authority:add',
        'PATCH': 'authority:update',
        'PUT': 'authority:update',
        'DELETE': 'authority:delete'
    }
