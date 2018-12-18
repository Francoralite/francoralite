# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
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


class CollectionViewSet(viewsets.ModelViewSet):
    """
    Collection management
    """

    queryset = CollectionModel.objects.all()
    serializer_class = CollectionSerializer

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
