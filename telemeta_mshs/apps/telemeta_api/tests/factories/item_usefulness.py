# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_usefulness factory to execute tests
"""

import factory
from ...models.item_usefulness import ItemUsefulness
# import nested/related factories
from .item import ItemFactory
from .usefulness import UsefulnessFactory


class ItemUsefulnessFactory(factory.django.DjangoModelFactory):
    """
    ItemUsefulness factory
    """

    class Meta:
        model = ItemUsefulness
        django_get_or_create = (
            'item',
            'usefulness',)

    # Nested/related factories
    item = factory.SubFactory(ItemFactory)
    usefulness = factory.SubFactory(UsefulnessFactory)
