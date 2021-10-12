# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import os
import mimetypes
import datetime
from django.http import Http404, HttpResponse
from django.conf import settings
import json
from wsgiref.util import FileWrapper


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from ..models.item import Item as ItemModel
from ..serializers.item import ItemSerializer


from ..models.item_collector import ItemCollector
from ..serializers.item_collector import ItemCollectorSerializer
from ..models.item_informer import ItemInformer
from ..serializers.item_informer import ItemInformerSerializer
from ..models.item_author import ItemAuthor
from ..serializers.item_author import ItemAuthorSerializer
from ..models.item_compositor import ItemCompositor
from ..models.item_dance import ItemDance
from ..serializers.item_dance import ItemDanceSerializer
from ..models.item_domain_music import ItemDomainMusic
from ..serializers.item_domain_music import ItemDomainMusicSerializer
from ..models.item_domain_song import ItemDomainSong
from ..serializers.item_domain_song import ItemDomainSongSerializer
from ..models.item_domain_tale import ItemDomainTale
from ..serializers.item_domain_tale import ItemDomainTaleSerializer
from ..models.item_domain_vocal import ItemDomainVocal
from ..serializers.item_domain_vocal import ItemDomainVocalSerializer
from ..models.item_language import ItemLanguage
from ..serializers.item_language import ItemLanguageSerializer
from ..models.item_thematic import ItemThematic
from ..serializers.item_thematic import ItemThematicSerializer
from ..models.item_usefulness import ItemUsefulness
from ..serializers.item_usefulness import ItemUsefulnessSerializer

from ..serializers.item_compositor import ItemCompositorSerializer
from ..models.item_musical_group import ItemMusicalGroup
from ..serializers.item_musical_group import ItemMusicalGroupSerializer
from ..models.item_musical_organization import ItemMusicalOrganization
from ..serializers.item_musical_organization import \
    ItemMusicalOrganizationSerializer
from ..models.performance_collection import PerformanceCollection
from ..models.performance_collection_musician import (
    PerformanceCollectionMusician)
from ..serializers.performance_collection import PerformanceCollectionSerializer  # noqa
from ..serializers.performance_collection_musician import (
    PerformanceCollectionMusicianSerializer)
from ..models.item_coirault import ItemCoirault
from ..serializers.item_coirault import ItemCoiraultSerializer

from ..models.recording_context import RecordingContext


entities = [
    {
        "names": "collectors", "name": "collector",
        "model": ItemCollector,
        "serializer": ItemCollectorSerializer
    },
    {
        "names": "informers", "name": "informer",
        "model": ItemInformer,
        "serializer": ItemInformerSerializer
    },
    {
        "names": "authors", "name": "author",
        "model": ItemAuthor,
        "serializer": ItemAuthorSerializer
    },
    {
        "names": "compositors", "name": "compositor",
        "model": ItemCompositor,
        "serializer": ItemCompositorSerializer
    },
    {
        "names": "dances", "name": "dance",
        "model": ItemDance,
        "serializer": ItemDanceSerializer
    },
    {
        "names": "domain_musics", "name": "domain_music",
        "model": ItemDomainMusic,
        "serializer": ItemDomainMusicSerializer
    },
    {
        "names": "domain_songs", "name": "domain_song",
        "model": ItemDomainSong,
        "serializer": ItemDomainSongSerializer
    },
    {
        "names": "domain_tales", "name": "domain_tale",
        "model": ItemDomainTale,
        "serializer": ItemDomainTaleSerializer
    },
    {
        "names": "domain_vocals", "name": "domain_vocal",
        "model": ItemDomainVocal,
        "serializer": ItemDomainVocalSerializer
    },
    {
        "names": "languages", "name": "language",
        "model": ItemLanguage,
        "serializer": ItemLanguageSerializer
    },
    {
        "names": "musical_groups", "name": "musical_group",
        "model": ItemMusicalGroup,
        "serializer": ItemMusicalGroupSerializer
    },
    {
        "names": "musical_organizations", "name": "musical_organization",
        "model": ItemMusicalOrganization,
        "serializer": ItemMusicalOrganizationSerializer
    },
    {
        "names": "thematics", "name": "thematic",
        "model": ItemThematic,
        "serializer": ItemThematicSerializer
    },
    {
        "names": "usefulnesses", "name": "usefulness",
        "model": ItemUsefulness,
        "serializer": ItemUsefulnessSerializer
    },
    {
        "names": "coiraults", "name": "coirault",
        "model": ItemCoirault,
        "serializer": ItemCoiraultSerializer
    },
]


class ItemViewSet(viewsets.ModelViewSet):
    """
    Item management
    """
    parser_classes = (FormParser, MultiPartParser,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer

    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    
    filterset_fields = ('collection', 'media_type', 'code', 'media_type',)
    ordering = ('code', 'title',)
    search_fields = ('title',)

    keycloak_scopes = {
        'GET': 'item:view',
        'POST': 'item:add',
        'PATCH': 'item:update',
        'PUT': 'item:update',
        'DELETE': 'item:delete'
    }

    def collect(self, id_main, data, entity):
        # Obtain the related records for an ID (id_main)
        items = entity["model"].objects.filter(
            item=id_main)
        # Create an empty list
        data[entity["names"]] = []
        # Parse every record
        for item in items:
            try:
                # Use the wanted serializer
                serializer_item = entity["serializer"](item)
                # Append the serialized data to the list
                data[entity["names"]].append(
                    serializer_item.data[entity["name"]])
            except Exception:
                pass

    @action(detail=True)
    def complete(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
       
        # Retrieve most of the entities
        for entity in entities:
            self.collect(instance.id, data, entity)

        # Retrieve the performances
        performances = PerformanceCollection.objects.filter(
            collection=instance.collection.id)
        data["performances"] = []
        for performance in performances:
            serializer_performance = PerformanceCollectionSerializer(performance)  # noqa
            data_performance = serializer_performance.data
            # Don't retrieve all the collection proerties -> only the ID
            data_performance["collection"] = instance.collection.id

            # Retrieve the musicians
            data_performance["musicians"] = []
            musicians = PerformanceCollectionMusician.objects.filter(
                performance_collection=performance.id)
            for musician in musicians:
                serializer_musician = PerformanceCollectionMusicianSerializer(
                    musician)
                data_performance["musicians"].append(
                    serializer_musician.data["musician"])

            data["performances"].append(data_performance)

        return Response(data)

    @action(detail=True)
    def performances(self, request, pk=None):
        instance = self.get_object()
        data = {}

        # Retrieve the performances
        performances = PerformanceCollection.objects.filter(
            collection=instance.collection.id)
        data["performances"] = []
        for performance in performances:
            serializer_performance = PerformanceCollectionSerializer(performance)  # noqa
            data_performance = serializer_performance.data
            # Don't retrieve all the collection proerties -> only the ID
            data_performance["collection"] = instance.collection.id

            # Retrieve the musicians
            data_performance["musicians"] = []
            musicians = PerformanceCollectionMusician.objects.filter(
                performance_collection=performance.id)
            for musician in musicians:
                serializer_musician = PerformanceCollectionMusicianSerializer(
                    musician)
                data_performance["musicians"].append(
                    serializer_musician.data["musician"])

            data["performances"].append(data_performance)

        return Response(data)

    @action(
        detail=True,
        methods=['get'],
        url_path='download', # noqa
        url_name='sound_download')
    def download(self, request, pk=None):
        instance = self.get_object()
        media = str(instance.file)
        filename = ""
        if media.find(settings.MEDIA_ROOT) == 0 :
            filename = media
        else:
            filename = settings.MEDIA_ROOT + media
        document = open( filename, 'rb')
        response = HttpResponse(FileWrapper(document), content_type="audio/mpeg")
        response['Content-Disposition'] = f'attachement; filename="{media}"'
        return response
