
"""
CollectionCollectors factory to execute tests
"""

import factory
from ...models.collectioncollectors import CollectionCollectors
from .collection import CollectionFactory
from .authority import AuthorityFactory


class CollectionCollectorsFactory(factory.django.DjangoModelFactory):
    """
    CollectionCollectors factory
    """

    class Meta:
        model = CollectionCollectors
        django_get_or_create = (
            'collection',
            'collector',)

    collection = factory.SubFactory(CollectionFactory)
    collector = factory.SubFactory(AuthorityFactory)
