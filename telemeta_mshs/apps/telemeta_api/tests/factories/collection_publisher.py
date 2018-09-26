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
# Import nested/related factories
from .MediaCollection import MediacollectionFactory
from .authority import AuthorityFactory


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
    collection = factory.SubFactory(MediacollectionFactory)
    publisher = factory.SubFactory(AuthorityFactory)
