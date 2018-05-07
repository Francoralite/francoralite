"""
location_type factory to execute tests
"""

import factory
from telemeta.models.location import LocationType

class LocationTypeFactory(factory.django.DjangoModelFactory):
    """
    LocationType factory
    """

    class Meta:
        model = LocationType
        django_get_or_create = ('code',)

    code = factory.Faker('word')
    name = factory.Faker('word')
