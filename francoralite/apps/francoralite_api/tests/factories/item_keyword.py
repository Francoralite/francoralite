# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_keyword factory to execute tests
"""

import factory
from ...models.item_keyword import ItemKeyword
# import nested/related factories
from .keyword import KeywordFactory


class ItemKeywordFactory(factory.django.DjangoModelFactory):
    """
    ItemKeyword factory
    """

    class Meta:
        model = ItemKeyword
        django_get_or_create = (
            'item',
            'keyword',)

    # Nested/related factories
    item = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")
    keyword = factory.SubFactory(KeywordFactory)
