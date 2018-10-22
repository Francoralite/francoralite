
"""
authority factory to execute tests
"""

import factory
from ...models.authority import Authority
from .location_gis import LocationGisFactory


class AuthorityFactory(factory.django.DjangoModelFactory):
    """
    Authority factory
    """

    class Meta:
        model = Authority

    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    civility = factory.Faker('prefix')
    alias = factory.Faker('word')
    is_collector = factory.Faker('boolean')
    is_informer = factory.Faker('boolean')
    is_author = factory.Faker('boolean')
    is_composer = factory.Faker('boolean')
    is_editor = factory.Faker('boolean')
    birth_date = factory.Faker('date')
    birth_location = factory.SubFactory(LocationGisFactory)
    death_date = factory.Faker('date')
    death_location = factory.SubFactory(LocationGisFactory)
    biography = factory.Faker('paragraph', nb_sentences=5)
    uri = factory.Faker('uri')
