# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_thematic factory to execute tests
"""

import factory
from ...models.item_thematic import ItemThematic
# import nested/related factories
from .item import ItemFactory
from .thematic import ThematicFactory


class ItemThematicFactory(factory.django.DjangoModelFactory):
    """
    ItemThematic factory
    """

    class Meta:
        model = ItemThematic
        django_get_or_create = (
            'item',
            'thematic',)

    # Nested/related factories
    item = factory.SubFactory(ItemFactory)
    thematic = factory.SubFactory(ThematicFactory)
