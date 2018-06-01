
"""
MediaCollection factory to execute tests
"""

import factory
from telemeta.models.collection import MediaCollection as Mediacollection
from .enumeration import (
    RecordingContextFactory,
    PublisherFactory,
    PublisherCollectionFactory,
    LegalRightsFactory,
    AcquisitionModeFactory,
    CopyTypeFactory,
    MetadataAuthorFactory,
    PublishingStatusFactory,
    StatusFactory,
    MetadataWriterFactory,
    MediatypeFactory,
    OriginalFormatFactory,
    PhysicalFormatFactory,
    AdconversionFactory)


class MediacollectionFactory(factory.django.DjangoModelFactory):
    """
    Mediacollection factory
    """

    class Meta:
        model = Mediacollection
        django_get_or_create = ('title',)

    # FIXIT------------------
    title = factory.Faker('word')
    alt_title = factory.Faker('word')
    creator = factory.Faker('word')
    description = factory.Faker('paragraph', nb_sentences=5)

    recording_context = factory.SubFactory(RecordingContextFactory)
    recorded_from_year = factory.Faker('year')
    recorded_to_year = factory.Faker('year')
    year_published = factory.Faker('year')
    public_access = factory.Faker('word')

    collector = factory.Faker('word')
    publisher = factory.SubFactory(PublisherFactory)
    publisher_collection = factory.SubFactory(PublisherCollectionFactory)
    publisher_serial = factory.Faker('word')
    booklet_author = factory.Faker('word')
    reference = factory.Faker('word')
    external_references = factory.Faker('paragraph', nb_sentences=5)

    auto_period_access = factory.Faker('boolean')
    legal_rights = factory.SubFactory(LegalRightsFactory)

    code = factory.Sequence(lambda n: 'code{0}'.format(n))
    old_code = factory.Faker('word')
    acquisition_mode = factory.SubFactory(AcquisitionModeFactory)
    cnrs_contributor = factory.Faker('word')
    copy_type = factory.SubFactory(CopyTypeFactory)
    metadata_author = factory.SubFactory(MetadataAuthorFactory)
    booklet_description = factory.Faker('paragraph', nb_sentences=3)
    publishing_status = factory.SubFactory(PublishingStatusFactory)
    status = factory.SubFactory(StatusFactory)
    alt_copies = factory.Faker('paragraph', nb_sentences=3)
    comment = factory.Faker('paragraph', nb_sentences=5)
    metadata_writer = factory.SubFactory(MetadataWriterFactory)
    archiver_notes = factory.Faker('paragraph', nb_sentences=3)
    items_done = factory.Faker('word')
    collector_is_creator = factory.Faker('boolean')
    is_published = factory.Faker('boolean')
    conservation_site = factory.Faker('word')

    media_type = factory.SubFactory(MediatypeFactory)
    approx_duration = '00:20:00'
    physical_items_num = factory.Faker('pyint')
    original_format = factory.SubFactory(OriginalFormatFactory)
    physical_format = factory.SubFactory(PhysicalFormatFactory)
    ad_conversion = factory.SubFactory(AdconversionFactory)

    alt_ids = factory.Faker('word')
    travail = factory.Faker('word')
