
"""
extMediaCollection factory to execute tests
"""

import factory
from ...models.collection import Collection
from .location_gis import LocationGisFactory
from .mediatype import MediaTypeFactory
from .legalrights import LegalRightsFactory
from .publisher import PublisherFactory
from .acquisition_mode import AcquisitionModeFactory
from .recording_context import RecordingContextFactory
from .collectioncollectors import CollectionCollectorsFactory
from .collection_informer import CollectionInformerFactory
from .collection_location import CollectionLocationFactory
from .collection_language import CollectionLanguageFactory
from .collection_publisher import CollectionPublisherFactory
from .performancecollectionmusician import PerformanceCollectionMusicianFactory
from .performancecollection import PerformanceCollectionFactory
from .item import ItemFactory



class CollectionFactory(factory.django.DjangoModelFactory):
    """
    Collection factory
    """
    code = factory.Sequence(lambda n: 'code{0}'.format(n))

    class Meta:
        model = Collection

    mission = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.fond.MissionFactory")
    title = factory.Faker('word')
    alt_title = factory.Faker('word')
    description = factory.Faker('paragraph', nb_sentences=5)
    # descriptions = factory.Faker('paragraph', nb_sentences=5)

    recording_context = factory.Faker('word')
    recorded_from_year = factory.Faker('date')
    recorded_to_year = factory.Faker('date')
    year_published = factory.Faker('year')

    # location = factory.SubFactory(LocationGisFactory)
    location_details = factory.Faker('paragraph', nb_sentences=3)
    cultural_area = factory.Faker('paragraph', nb_sentences=1)
    language = factory.Faker('word')

    # publisher = factory.SubFactory(PublisherFactory)
    # publisher = factory.Faker('word')
    # publisher_collection = factory.SubFactory(CollectionPublisherFactory)
    publisher_collection = factory.Faker('word')
    booklet_author = factory.Faker('word')
    metadata_author = factory.Faker('word')
    code_partner = factory.Faker('word')
    booklet_description = factory.Faker('paragraph', nb_sentences=3)
    comment = factory.Faker('paragraph', nb_sentences=5)
    media_type = factory.SubFactory(MediaTypeFactory)
    physical_items_num = factory.Faker('pyint')
    auto_period_access = factory.Faker('boolean')
    legal_rights = factory.SubFactory(LegalRightsFactory)
    # public_access = factory.Faker('word')


class CollectionCompleteFactory(CollectionFactory):
    """
    Collection with all related entities
    """

    @factory.post_generation
    def complete( self, create, extracted, **kwargs):
        if not create: return

        CollectionCollectorsFactory.create_batch(2, collection = self)
        CollectionInformerFactory.create_batch(2, collection = self)
        CollectionLocationFactory.create_batch(2, collection = self)
        CollectionLanguageFactory.create_batch(2, collection = self)
        CollectionPublisherFactory.create_batch(2, collection = self)
        perfs = PerformanceCollectionFactory.create_batch(2, collection = self)

        for perf in perfs:
            PerformanceCollectionMusicianFactory.create_batch(
                2, performance_collection = perf)
            
class CollectionItemsFactory(CollectionFactory):
    """
    Collection with items related
    """

    @factory.post_generation
    def items( self, create, extracted, **kwargs):
        if not create: return

        ItemFactory.create_batch(5, collection = self)
