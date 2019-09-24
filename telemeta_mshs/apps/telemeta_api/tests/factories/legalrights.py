
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

    name = factory.Faker('sentence', nb_words=3)
    notes = factory.Faker('paragraph', nb_sentences=1)
