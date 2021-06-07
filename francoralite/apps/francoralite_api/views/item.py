# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import os
import mimetypes
import datetime
from django.http import Http404, HttpResponse, StreamingHttpResponse
from django.conf import settings
import json


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

    filterset_fields = ('collection', 'media_type',)
    ordering = ('title', 'code',)
    search_fields = ('title', 'code', 'collection', 'media_type')

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


    def stream_from_file(self, file):
        chunk_size = 0x100000
        f = open(file, 'r')
        while True:
            chunk = f.read(chunk_size)
            if not len(chunk):
                f.close()
                break
            yield chunk

    def serve_media(self, filename, content_type="", buffering=True):
        if not settings.DEBUG:
            return self.nginx_media_accel(filename, content_type=content_type,
                                    buffering=buffering)
        else:
            response = StreamingHttpResponse(self.stream_from_file(filename), content_type=content_type)
            response['Content-Disposition'] = 'attachment; ' + 'filename=' + filename
            return response

    def nginx_media_accel(self, media_path, content_type="", buffering=True):
        """Send a protected media file through nginx with X-Accel-Redirect"""

        response = HttpResponse()
        url = settings.MEDIA_URL + os.path.relpath(media_path, settings.MEDIA_ROOT)
        filename = os.path.basename(media_path)
        response['Content-Disposition'] = "attachment; filename=%s" % (filename)
        response['Content-Type'] = content_type
        response['X-Accel-Redirect'] = url

        if not buffering:
            response['X-Accel-Buffering'] = 'no'
            #response['X-Accel-Limit-Rate'] = 524288

        return response

    @action(
        detail=True,
        methods=['get'],
        url_path='download/(?P<file_name>[a-zA-Z0-9_.]+)', # noqa
        url_name='sound_download')
    def download(self, request, pk=None, file_name=""):
        item = ItemModel.objects.get(id=pk)
        #media = self.item_transcode(item=item, extension="mp3")
        #response = serve_media(media[0], content_type=media[1])
        file = item.public_id + '.mp3'
        media = settings.MEDIA_ROOT + os.sep + file
        response = self.serve_media(media, content_type="mp3")
        return response
