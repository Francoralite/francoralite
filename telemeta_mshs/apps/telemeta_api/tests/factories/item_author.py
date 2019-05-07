# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_author factory to execute tests
"""

import factory
from ...models.item_author import ItemAuthor
# import nested/related factories
from .item import ItemFactory
from .authority import AuthorityFactory


class ItemAuthorFactory(factory.django.DjangoModelFactory):
    """
    ItemAuthor factory
    """

    class Meta:
        model = ItemAuthor
        django_get_or_create = (
            'item',
            'author',)

    # Nested/related factories
    item = factory.SubFactory(ItemFactory)
    author = factory.SubFactory(AuthorityFactory)
