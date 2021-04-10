# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
item_language factory to execute tests
"""

import factory
from ...models.item_language import ItemLanguage
# import nested/related factories
from .language import LanguageFactory


class ItemLanguageFactory(factory.django.DjangoModelFactory):
    """
    ItemLanguage factory
    """

    class Meta:
        model = ItemLanguage
        django_get_or_create = (
            'item',
            'language',)

    # Nested/related factories
    item = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.item.ItemFactory")
    language = factory.SubFactory(LanguageFactory)