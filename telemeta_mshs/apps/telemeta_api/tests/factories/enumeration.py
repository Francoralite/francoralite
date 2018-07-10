"""
Enumeration factory to execute tests
"""

import factory
from telemeta.models.enum import (
    Enumeration,
    RecordingContext,
    Publisher,
    PublisherCollection,
    LegalRight,
    AcquisitionMode,
    CopyType,
    MetadataAuthor,
    PublishingStatus,
    Status,
    MetadataWriter,
    MediaType,
    OriginalFormat,
    PhysicalFormat,
    AdConversion
    )


class EnumerationFactory(factory.django.DjangoModelFactory):
    """
    Enumeration factory
    """

    class Meta:
        model = Enumeration
        abstract = True
        django_get_or_create = ('value', )

    value = factory.Faker('word')
    notes = factory.Faker('paragraph', nb_sentences=2)


class RecordingContextFactory(EnumerationFactory):
    class Meta:
        model = RecordingContext


class PublisherFactory(EnumerationFactory):
    class Meta:
        model = Publisher


class PublisherCollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PublisherCollection

    publisher = factory.SubFactory(PublisherFactory)
    value = factory.Faker('word')


class LegalRightsFactory(EnumerationFactory):
    class Meta:
        model = LegalRight


class AcquisitionModeFactory(EnumerationFactory):
    class Meta:
        model = AcquisitionMode


class CopyTypeFactory(EnumerationFactory):
    class Meta:
        model = CopyType


class MetadataAuthorFactory (EnumerationFactory):
    class Meta:
        model = MetadataAuthor


class PublishingStatusFactory(EnumerationFactory):
    class Meta:
        model = PublishingStatus


class StatusFactory(EnumerationFactory):
    class Meta:
        model = Status


class MetadataWriterFactory(EnumerationFactory):
    class Meta:
        model = MetadataWriter


class MediatypeFactory(EnumerationFactory):
    class Meta:
        model = MediaType


class OriginalFormatFactory(EnumerationFactory):
    class Meta:
        model = OriginalFormat


class PhysicalFormatFactory(EnumerationFactory):
    class Meta:
        model = PhysicalFormat


class AdconversionFactory(EnumerationFactory):
    class Meta:
        model = AdConversion
