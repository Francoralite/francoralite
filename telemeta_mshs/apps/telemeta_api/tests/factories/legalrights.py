
"""
coupe factory to execute tests
"""

import factory
from ...models.legal_rights import LegalRights


class LegalRightsFactory(factory.django.DjangoModelFactory):
    """
    Legal rights factory
    """

    class Meta:
        model = LegalRights

    name = factory.Sequence(lambda n: 'legal%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
