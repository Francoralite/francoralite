
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

    name = factory.Sequence(lambda n: 'coupe%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
