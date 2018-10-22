
"""
location factory to execute tests
"""

import factory
from ...models.location import Location


class LocationGisFactory(factory.django.DjangoModelFactory):
    """
    Location GIS factory
    """

    class Meta:
        model = Location
        django_get_or_create = ('name',)

    code = factory.Faker('word')
    name = factory.Faker('word')
    notes = factory.Faker('paragraph', nb_sentences=1)
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
