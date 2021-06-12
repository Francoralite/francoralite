
"""
Emit_vox factory to execute tests
"""

import factory
from ...models.emit_vox import EmitVox


class EmitVoxFactory(factory.django.DjangoModelFactory):
    """
    Emit_vox factory
    """

    class Meta:
        model = EmitVox

    name = factory.Sequence(lambda n: 'emit%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)