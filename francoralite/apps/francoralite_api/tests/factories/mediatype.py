
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

    name = factory.Sequence(lambda n: 'media%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
