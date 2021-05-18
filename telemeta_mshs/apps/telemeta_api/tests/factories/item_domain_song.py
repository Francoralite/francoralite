# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_domain_song factory to execute tests
"""

import factory
from ...models.item_domain_song import ItemDomainSong
# import nested/related factories
from .domain_song import DomainSongFactory


class ItemDomainSongFactory(factory.django.DjangoModelFactory):
    """
    ItemDomainSong factory
    """

    class Meta:
        model = ItemDomainSong
        django_get_or_create = (
            'item',
            'domain_song',)

    # Nested/related factories
    item = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.item.ItemFactory")
    domain_song = factory.SubFactory(DomainSongFactory)
