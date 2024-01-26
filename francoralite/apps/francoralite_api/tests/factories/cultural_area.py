
"""
CulturalArea factory to execute tests
"""

import factory
from ...models.cultural_area import CulturalArea


class CulturalAreaFactory(factory.django.DjangoModelFactory):
    """
    CulturalArea factory
    """

    class Meta:
        model = CulturalArea

    name = factory.Sequence(lambda n: 'area%d' % n)
    geojson = factory.Faker('paragraph', nb_sentences=1)
