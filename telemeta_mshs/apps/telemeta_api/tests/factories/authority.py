
"""
authority factory to execute tests
"""

import factory
from ...models.authority import Authority
from .location import LocationFactory

ROLES = [role[0] for role in Authority.ROLES]


class AuthorityFactory(factory.django.DjangoModelFactory):
    """
    Authority factory
    """

    class Meta:
        model = Authority

    # FIXIT------------------
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    civilite = factory.Faker('prefix')
    alias = factory.Faker('word')
    roles = factory.Faker('random_element', elements=ROLES)
    birth_date = factory.Faker('date')
    birth_location = factory.SubFactory(LocationFactory)
    death_date = factory.Faker('date')
    death_location = factory.SubFactory(LocationFactory)
    biography = factory.Faker('paragraphs')
    uri = factory.Faker('uri_page')
