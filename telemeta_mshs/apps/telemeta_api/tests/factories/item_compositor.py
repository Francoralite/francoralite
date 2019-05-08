# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_compositor factory to execute tests
"""

import factory
from ...models.item_compositor import ItemCompositor
# import nested/related factories
from .item import ItemFactory
from .authority import AuthorityFactory


class ItemCompositorFactory(factory.django.DjangoModelFactory):
    """
    ItemCompositor factory
    """

    class Meta:
        model = ItemCompositor
        django_get_or_create = (
            'item',
            'compositor',)

    # Nested/related factories
    item = factory.SubFactory(ItemFactory)
    compositor = factory.SubFactory(AuthorityFactory)
