
"""
location factory to execute tests
"""

import factory
from telemeta.models.location import Location
from .location_type import LocationTypeFactory


class LocationFactory(factory.django.DjangoModelFactory):
    """
    Location factory
    """

    class Meta:
        model = Location
        django_get_or_create = ('name',)

    name = factory.Faker('word')
    type = 0
    complete_type = factory.SubFactory(LocationTypeFactory)
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    is_authoritative = factory.Faker('boolean')
