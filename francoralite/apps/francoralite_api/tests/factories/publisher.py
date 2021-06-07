
"""
coupe factory to execute tests
"""

import factory
from ...models.publisher import Publisher


class PublisherFactory(factory.django.DjangoModelFactory):
    """
    Publisher factory
    """

    class Meta:
        model = Publisher

    name = factory.Sequence(lambda n: 'publisher%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
