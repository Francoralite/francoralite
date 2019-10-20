
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

    name = factory.Faker('sentence', nb_words=3)
    notes = factory.Faker('paragraph', nb_sentences=1)
