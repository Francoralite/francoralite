# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
ItemTranscodingFlag factory to execute tests
"""

import factory
from ...models.item_transcoding_flag import ItemTranscodingFlag
from .item import ItemFactory


class ItemTranscodingFlagFactory(factory.django.DjangoModelFactory):
    """
    ItemTranscodingFlag factory
    """

    class Meta:
        model = ItemTranscodingFlag

    item = factory.SubFactory(ItemFactory)
    mime_type = factory.Faker('mime_type')
    date = factory.Faker('date_time_this_month')
    value = factory.Faker('boolean')
