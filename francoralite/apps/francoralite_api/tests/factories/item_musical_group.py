# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_musical_group factory to execute tests
"""

import factory
from ...models.item_musical_group import ItemMusicalGroup
# import nested/related factories
from .musical_group import MusicalGroupFactory


class ItemMusicalGroupFactory(factory.django.DjangoModelFactory):
    """
    ItemMusicalGroup factory
    """

    class Meta:
        model = ItemMusicalGroup
        django_get_or_create = (
            'item',
            'musical_group',)

    # Nested/related factories
    item = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")
    musical_group = factory.SubFactory(MusicalGroupFactory)
