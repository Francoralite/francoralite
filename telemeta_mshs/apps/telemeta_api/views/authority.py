from rest_framework import viewsets, filters
from ..models.authority import Authority as AuthorityModel
from ..serializers.authority import AuthoritySerializer


class AuthorityViewSet(viewsets.ModelViewSet):
    """
    Authority management
    """

    queryset = AuthorityModel.objects.all()
    serializer_class = AuthoritySerializer
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = (
        'is_collector', 'is_informer',
        'is_author', 'is_composer', 'is_editor')
    ordering = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name')
