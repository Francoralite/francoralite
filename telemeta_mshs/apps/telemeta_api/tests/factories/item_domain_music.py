# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_domain_music factory to execute tests
"""

import factory
from ...models.item_domain_music import ItemDomainMusic
# import nested/related factories
from .item import ItemFactory
from .domain_music import DomainMusicFactory


class ItemDomainMusicFactory(factory.django.DjangoModelFactory):
    """
    ItemDomainMusic factory
    """

    class Meta:
        model = ItemDomainMusic
        django_get_or_create = (
            'item',
            'domain_music',)

    # Nested/related factories
    item = factory.SubFactory(ItemFactory)
    domain_music = factory.SubFactory(DomainMusicFactory)
