# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_coirault factory to execute tests
"""

import factory
from ...models.item_coirault import ItemCoirault
# Import nested/related factories
from .item import ItemFactory
from .skos_concept import SkosConceptFactory


class ItemCoiraultFactory(factory.django.DjangoModelFactory):
    """
    ItemCoirault factory
    """

    class Meta:
        model = ItemCoirault
        django_get_or_create = (
            'item',
            'coirault',)

    # Nested/related factories
    item = factory.SubFactory(ItemFactory)
    coirault = factory.SubFactory(SkosConceptFactory)
