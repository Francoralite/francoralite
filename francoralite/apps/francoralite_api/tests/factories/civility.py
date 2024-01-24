
"""
civility factory to execute tests
"""

import factory
from ...models.civility import Civility


class CivilityFactory(factory.django.DjangoModelFactory):
    """
    Civility factory
    """

    class Meta:
        model = Civility

    name = factory.Sequence(lambda n: 'civility%d' % n)
