
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
        django_get_or_create = ('value',)

    value = factory.Faker('word')
    notes = factory.Faker('word')
