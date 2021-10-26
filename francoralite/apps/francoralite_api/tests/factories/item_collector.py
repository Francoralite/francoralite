# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_collector factory to execute tests
"""

import factory
from ...models.item_collector import ItemCollector


class ItemCollectorFactory(factory.django.DjangoModelFactory):
    """
    ItemCollector factory
    """

    class Meta:
        model = ItemCollector
        django_get_or_create = (
            'item',
            'collector',)

    # Nested/related factories
    item = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")
    collector = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.authority.AuthorityFactory")
