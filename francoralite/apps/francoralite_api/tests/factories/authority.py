
"""
authority factory to execute tests
"""

import factory
from ...models.authority import Authority
from .location_gis import LocationGisFactory
from .item_informer import ItemInformerFactory

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

class AuthorityContribsFactory(AuthorityFactory):
    """
    Authority factory with contibutions
    """
    @factory.post_generation
    def contribs( self, create, extracted, **kwargs):
        if not create: return

        ItemInformerFactory.create_batch(6, informer = self)
