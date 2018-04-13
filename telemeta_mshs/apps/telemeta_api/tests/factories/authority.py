
"""
authority factory to execute tests
"""

import factory
from ...models.authority import Authority


class AuthorityFactory(factory.Factory):
    """
    Authority factory
    """

    class Meta:
        model = Authority

    #fake = factory.Faker('fr_FR')
    # FIXIT------------------
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    civilite = factory.Faker('prefix')
    alias = factory.Faker('word')
    roles = factory.Faker('word')
    birth_date = factory.Faker('date')
    death_date = factory.Faker('date')
    biography = factory.Faker('paragraphs')
    uri = factory.Faker('uri_page')
    birth_location = None
    death_location = None
