
"""
extMediaCollection factory to execute tests
"""

import factory
from django.db.models import signals
from ...models.ext_media_collection import ExtMediaCollection
from .MediaCollection import MediacollectionFactory


# mute signal, because there's
#  a OneToOneField between MediaCollection and ExtMediaCollection
@factory.django.mute_signals(signals.post_save)
class ExtMediaCollectionFactory(factory.django.DjangoModelFactory):
    """
    ExtMediaCollection factory
    """

    class Meta:
        model = ExtMediaCollection
        django_get_or_create = (
            'media_collection',
            'location_details',
            'cultural_area',
            'language',)

    media_collection = factory.SubFactory(MediacollectionFactory)
    location_details = factory.Faker('paragraph', nb_sentences=3)
    cultural_area = factory.Faker('paragraph', nb_sentences=1)
    language = factory.Faker('word')
