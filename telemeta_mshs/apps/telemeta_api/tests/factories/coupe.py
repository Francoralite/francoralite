
"""
coupe factory to execute tests
"""

import factory
from ...models.coupe import Coupe


class CoupeFactory(factory.django.DjangoModelFactory):
    """
    Coupe factory
    """

    class Meta:
        model = Coupe
        django_get_or_create = ('value',)

    value = factory.Faker('word')
    notes = factory.Faker('word')
