"""
location_type factory to execute tests
"""

import factory
from telemeta.models.location import LocationType

class LocationTypeFactory(factory.Factory):
    """
    LocationType factory
    """

    class Meta:
        model = LocationType

    code = factory.Faker('word')
    name = factory.Faker('word')
