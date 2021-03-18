
"""
extMediaCollection factory to execute tests
"""

import factory
from ...models.collection import Collection
from .mission import MissionFactory
from .location_gis import LocationGisFactory
from .mediatype import MediaTypeFactory
from .legalrights import LegalRightsFactory
from .publisher import PublisherFactory
# from .collection_publisher import CollectionPublisherFactory
from .acquistion_mode import AcquisitionModeFactory
from .recording_context import RecordingContextFactory


class CollectionFactory(factory.django.DjangoModelFactory):
    """
    Collection factory
    """
    code = factory.Sequence(lambda n: 'code{0}'.format(n))

    class Meta:
        model = Collection

    mission = factory.SubFactory(MissionFactory)
    title = factory.Faker('word')
    alt_title = factory.Faker('word')
    description = factory.Faker('paragraph', nb_sentences=5)
    # descriptions = factory.Faker('paragraph', nb_sentences=5)

    recording_context = factory.SubFactory(RecordingContextFactory)
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
    # publisher_collection = factory.Faker('word')
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
