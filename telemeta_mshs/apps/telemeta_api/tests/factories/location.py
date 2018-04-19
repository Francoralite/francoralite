
"""
location factory to execute tests
"""

import factory
from telemeta.models.location import Location
from location_type import LocationTypeFactory


class LocationFactory(factory.Factory):
    """
    Location factory
    """

    class Meta:
        model = Location

    # FIXIT------------------
    name = factory.Faker('word')
    type = 0
    complete_type = factory.SubFactory(LocationTypeFactory)
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    is_authoritative = factory.Faker('boolean')
