# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
ItemMarker factory to execute tests
"""

import factory
import factory.fuzzy
from ...models.item_marker import ItemMarker
from .item import ItemFactory
from .user import UserFactory


class ItemMarkerFactory(factory.django.DjangoModelFactory):
    """
    ItemMarker factory
    """

    class Meta:
        model = ItemMarker

    item = factory.SubFactory(ItemFactory)
    time = factory.fuzzy.FuzzyFloat(300.0)
    title = factory.Faker('word')
    date = factory.Faker('date_time', locale="fr_FR")
    description = factory.Faker('paragraph', nb_sentences=1)
    # FIXIT------------------
    # author = factory.SubFactory(UserFactory)
