# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_musical_organization factory to execute tests
"""

import factory
from ...models.item_musical_organization import ItemMusicalOrganization
# import nested/related factories
from .item import ItemFactory
from .musical_organization import MusicalOrganizationFactory


class ItemMusicalOrganizationFactory(factory.django.DjangoModelFactory):
    """
    ItemMusicalOrganization factory
    """

    class Meta:
        model = ItemMusicalOrganization
        django_get_or_create = (
            'item',
            'musical_organization',)

    # Nested/related factories
    item = factory.SubFactory(ItemFactory)
    musical_organization = factory.SubFactory(MusicalOrganizationFactory)
