"""
Institution factory to execute tests
"""

import factory
from ...models.institution import Institution


class InstitutionFactory(factory.Factory):
    """
    Institution factory
    """

    class Meta:
        model = Institution

    name = factory.Faker('word')
    notes = factory.Faker('word')
