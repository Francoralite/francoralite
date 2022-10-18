
"""
block factory to execute tests
"""

import factory
from ...models.block import Block


class BlockFactory(factory.django.DjangoModelFactory):
    """
    Block factory
    """

    class Meta:
        model = Block

    type = factory.Sequence(lambda n: 'M' if n == 3 else 'P' if n == '4' else None)
    title = factory.Sequence(lambda n: 'block%d' % n)
    content = factory.Faker('paragraph', nb_sentences=5)
    order = factory.Sequence(lambda n: 3 - n if n <= 3 else n)
    show = factory.Faker('boolean')
