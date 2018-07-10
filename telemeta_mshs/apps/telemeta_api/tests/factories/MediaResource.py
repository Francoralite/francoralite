
"""
MediaResource factory to execute tests
"""

import factory
from telemeta.models.resource import MediaResource


class MediaresourceFactory(factory.Factory):
    """
    Mediaresource factory
    """

    class Meta:
        model = MediaResource
