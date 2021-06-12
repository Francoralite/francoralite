# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
collection_informer factory to execute tests
"""

import factory
from ...models.collection_informer import CollectionInformer
from .authority import AuthorityFactory


class CollectionInformerFactory(factory.django.DjangoModelFactory):
    """
    CollectionInformer factory
    """

    class Meta:
        model = CollectionInformer
        django_get_or_create = (
            'collection',
            'informer',)

    # Nested/related factories
    collection = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.collection.CollectionFactory")
    informer = factory.SubFactory(AuthorityFactory)
