# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
ItemFunction factory to execute tests
"""

import factory
from ...models.item_function import ItemFunction


class ItemFunctionFactory(factory.django.DjangoModelFactory):
    """
    ItemFunction factory
    """

    class Meta:
        model = ItemFunction

    name = factory.Faker('sentence', nb_words=3)
    notes = factory.Faker('paragraph', nb_sentences=1)
