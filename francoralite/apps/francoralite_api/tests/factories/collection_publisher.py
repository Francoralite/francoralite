# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
collection_publisher factory to execute tests
"""

import factory
from ...models.collection_publisher import CollectionPublisher

from .publisher import PublisherFactory


class CollectionPublisherFactory(factory.django.DjangoModelFactory):
    """
    CollectionPublisher factory
    """

    class Meta:
        model = CollectionPublisher
        django_get_or_create = (
            'collection',
            'publisher',)

    # Nested/related factories
    collection = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.collection.CollectionFactory")
    publisher = factory.SubFactory(PublisherFactory)
