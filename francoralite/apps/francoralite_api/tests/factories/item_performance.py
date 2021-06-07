# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_performance factory to execute tests
"""

import factory
from ...models.item_performance import ItemPerformance
# import nested/related factories
from .performancecollection import PerformanceCollectionFactory

class ItemPerformanceFactory(factory.django.DjangoModelFactory):
    """
    ItemPerformance factory
    """

    class Meta:
        model = ItemPerformance
        django_get_or_create = (
            'item',
            'performance',)

    # Nested/related factories
    item = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")
    performance = factory.SubFactory(PerformanceCollectionFactory)