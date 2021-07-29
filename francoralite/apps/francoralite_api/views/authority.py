from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models.authority import Authority as AuthorityModel
from ..models.item_informer import ItemInformer
from ..models.item_collector import ItemCollector
from ..models.item_author import ItemAuthor
from ..models.item_compositor import ItemCompositor
from ..serializers.authority import AuthoritySerializer
from ..serializers.item_informer import ItemInformerSerializer
from ..serializers.item_collector import ItemCollectorSerializer
from ..serializers.item_author import ItemAuthorSerializer
from ..serializers.item_compositor import ItemCompositorSerializer


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
        item_informers = ItemInformer.objects.filter( informer=instance.id )
        for item_informer in item_informers :
            serializer_informer = ItemInformerSerializer( item_informer )
            data["informers"].append( serializer_informer.data["item"] )

        # Retrieve the item collectors
        data["collectors"] = []
        item_collectors = ItemCollector.objects.filter( collector=instance.id )
        for item_collector in item_collectors :
            serializer_collector = ItemCollectorSerializer( item_collector )
            data["collectors"].append( serializer_collector.data["item"] )

        # Retrieve the item authors
        data["authors"] = []
        item_authors = ItemAuthor.objects.filter( author=instance.id )
        for item_author in item_authors :
            serializer_author = ItemAuthorSerializer( item_author )
            data["authors"].append( serializer_author.data["item"] ) 

        # Retrieve the item compositors
        data["compositors"] = []
        item_compositors = ItemCompositor.objects.filter( compositor=instance.id )
        for item_compositor in item_compositors :
            serializer_compositor = ItemCompositorSerializer( item_compositor )
            data["compositors"].append( serializer_compositor.data["item"] )

        return Response(data)