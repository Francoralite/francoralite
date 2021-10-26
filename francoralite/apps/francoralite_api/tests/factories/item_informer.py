# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_informer factory to execute tests
"""

import factory
from ...models.item_informer import ItemInformer


class ItemInformerFactory(factory.django.DjangoModelFactory):
    """
    ItemInformer factory
    """

    class Meta:
        model = ItemInformer
        django_get_or_create = (
            'item',
            'informer',)

    # Nested/related factories
    item = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")
    informer = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.authority.AuthorityFactory")

