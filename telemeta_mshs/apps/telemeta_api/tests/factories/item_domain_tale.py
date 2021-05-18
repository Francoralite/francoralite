# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_domain_tale factory to execute tests
"""

import factory
from ...models.item_domain_tale import ItemDomainTale
# import nested/related factories
from .domain_tale import DomainTaleFactory


class ItemDomainTaleFactory(factory.django.DjangoModelFactory):
    """
    ItemDomainTale factory
    """

    class Meta:
        model = ItemDomainTale
        django_get_or_create = (
            'item',
            'domain_tale',)

    # Nested/related factories
    item = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.item.ItemFactory")
    domain_tale = factory.SubFactory(DomainTaleFactory)
