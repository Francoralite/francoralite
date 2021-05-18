
"""
coupe factory to execute tests
"""

import factory
from ...models.recording_context import RecordingContext


class RecordingContextFactory(factory.django.DjangoModelFactory):
    """
    Recording context factory
    """

    class Meta:
        model = RecordingContext

    name = factory.Sequence(lambda n: 'context%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
