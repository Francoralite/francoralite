from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models.authority import Authority as AuthorityModel
from ..models.item_informer import ItemInformer
from ..serializers.authority import AuthoritySerializer
from ..serializers.item_informer import ItemInformerSerializer


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

    @action(detail=True)
    def contribs(self, request, pk=None):

        instance = self.get_object()
        data = {}

        # Retrieve the item informers
        data["informers"] = []
        item_informers = ItemInformer.objects.filter(informer=instance.id)
        for item_informer in item_informers :
            serializer_informer = ItemInformerSerializer(item_informer)
            data["informers"].append( serializer_informer.data["item"])

        return Response(data)