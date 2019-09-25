# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from ..models.collection import Collection as CollectionModel
from ..models.collectioncollectors import CollectionCollectors
from ..models.collection_informer import CollectionInformer
from ..models.collection_location import CollectionLocation
from ..models.collection_language import CollectionLanguage
from ..models.collection_publisher import CollectionPublisher
from ..models.performance_collection import PerformanceCollection
from ..models.performance_collection_musician import (
    PerformanceCollectionMusician)
from ..serializers.collection import CollectionSerializer
from ..serializers.collection_informer import CollectionInformerSerializer
from ..serializers.collectioncollectors import CollectionCollectorsSerializer
from ..serializers.collection_location import CollectionLocationSerializer
from ..serializers.collection_language import CollectionLanguageSerializer
from ..serializers.collection_publisher import CollectionPublisherSerializer
from ..serializers.performance_collection import PerformanceCollectionSerializer  # noqa
from ..serializers.performance_collection_musician import (
    PerformanceCollectionMusicianSerializer)


entities = [
    {
        "names": "collectors", "name": "collector",
        "model": CollectionCollectors,
        "serializer": CollectionCollectorsSerializer
    },
    {
        "names": "informers", "name": "informer",
        "model": CollectionInformer,
        "serializer": CollectionInformerSerializer
    },
    {
        "names": "locations", "name": "location",
        "model": CollectionLocation,
        "serializer": CollectionLocationSerializer
    },
    {
        "names": "languages", "name": "language",
        "model": CollectionLanguage,
        "serializer": CollectionLanguageSerializer
    },
    {
        "names": "publishers", "name": "publisher",
        "model": CollectionPublisher,
        "serializer": CollectionPublisherSerializer
    }
]


class CollectionViewSet(viewsets.ModelViewSet):
    """
    Collection management
    """

    queryset = CollectionModel.objects.all()
    serializer_class = CollectionSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('mission',)
    ordering = ('mission', 'code')
    search_fields = ('mission', 'code', 'title')

    keycloak_scopes = {
        'GET': 'collection:view',
        'POST': 'collection:add',
        'PATCH': 'collection:update',
        'PUT': 'collection:update',
        'DELETE': 'collection:delete'
    }

    def collect(self, id_main, data, entity):
        items = entity["model"].objects.filter(
            collection=id_main)
        data[entity["names"]] = []
        for item in items:
            serializer_item = entity["serializer"](item)
            data[entity["names"]].append(serializer_item.data[entity["name"]])

    @detail_route()
    def complete(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        # Retrieve most of the entities
        for entity in entities:
            self.collect(instance.id, data, entity)

        # Retrieve the performances
        performances = PerformanceCollection.objects.filter(
            collection=instance.id)
        data["performances"] = []
        for performance in performances:
            serializer_performance = PerformanceCollectionSerializer(performance)  # noqa
            data_performance = serializer_performance.data
            # Don't retrieve all the collection proerties -> only the ID
            data_performance["collection"] = instance.id

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

    def perform_destroy(self, instance):

        # Delete the collectors
        collectors = CollectionCollectors.objects.filter(
            collection=instance.id)
        for collector in collectors:
            collector.delete()

        # Delete the informers
        informers = CollectionInformer.objects.filter(
            collection=instance.id)
        for informer in informers:
            informer.delete()

        # Delete the locations
        locations = CollectionLocation.objects.filter(
            collection=instance.id)
        for location in locations:
            location.delete()

        # Delete the languages
        languages = CollectionLanguage.objects.filter(
            collection=instance.id)
        for language in languages:
            language.delete()

        # Delete the publishers
        publishers = CollectionPublisher.objects.filter(
            collection=instance.id)
        for publisher in publishers:
            publisher.delete()

        # Delete the performances
        performances = PerformanceCollection.objects.filter(
            collection=instance.id)
        for performance in performances:
            # Delete the musicians
            musicians = PerformanceCollectionMusician.objects.filter(
                performance_collection=performance.id)
            for musician in musicians:
                musician.delete()
            performance.delete()

        instance.delete()
