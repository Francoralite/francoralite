# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_domain_vocal factory to execute tests
"""

import factory
from ...models.item_domain_vocal import ItemDomainVocal
# import nested/related factories
from .domain_vocal import DomainVocalFactory


class ItemDomainVocalFactory(factory.django.DjangoModelFactory):
    """
    ItemDomainVocal factory
    """

    class Meta:
        model = ItemDomainVocal
        django_get_or_create = (
            'item',
            'domain_vocal',)

    # Nested/related factories
    item = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")
    domain_vocal = factory.SubFactory(DomainVocalFactory)
