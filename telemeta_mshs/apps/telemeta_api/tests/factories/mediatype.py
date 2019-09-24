
"""
mediatype factory to execute tests
"""

import factory
from ...models.mediatype import MediaType


class MediaTypeFactory(factory.django.DjangoModelFactory):
    """
    Mediatype factory
    """

    class Meta:
        model = MediaType

    name = factory.Faker('sentence', nb_words=3)
    notes = factory.Faker('paragraph', nb_sentences=1)
