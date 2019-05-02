# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
ItemAnalysis factory to execute tests
"""

import factory
from ...models.item_analysis import ItemAnalysis
from .item import ItemFactory


class ItemAnalysisFactory(factory.django.DjangoModelFactory):
    """
    ItemAnalysis factory
    """

    class Meta:
        model = ItemAnalysis

    element_type = "analysis"
    item = factory.SubFactory(ItemFactory)
    analyzer_id = factory.Faker('word')
    name = factory.Faker('word')
    value = factory.Faker('word')
    unit = factory.Faker('word')
