# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_dance factory to execute tests
"""

import factory
from ...models.item_dance import ItemDance
# import nested/related factories
from .dance import DanceFactory


class ItemDanceFactory(factory.django.DjangoModelFactory):
    """
    ItemDance factory
    """

    class Meta:
        model = ItemDance
        django_get_or_create = (
            'item',
            'dance',)

    # Nested/related factories
    item = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.item.ItemFactory")
    dance = factory.SubFactory(DanceFactory)
