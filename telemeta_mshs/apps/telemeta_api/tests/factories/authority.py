
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

    fake = factory.Faker('fr_FR')
    # FIXIT------------------
    last_name = fake.last_name()
    first_name = fake.last_name()
    civilite = fake.prefix()
    alias = fake.word()
    roles = fake.word()
    birth_date = fake.date()
    death_date = fake.date()
    biography = fake.paragraphs(nb=3)
    uri = fake.uri_page()
