# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
collection_language factory to execute tests
"""

import factory
from ...models.collection_language import CollectionLanguage
# Import nested/related factories
from .collection import CollectionFactory
from .language import LanguageFactory


class CollectionLanguageFactory(factory.django.DjangoModelFactory):
    """
    CollectionLanguage factory
    """

    class Meta:
        model = CollectionLanguage
        django_get_or_create = (
            'collection',
            'language',)

    # Nested/related factories
    collection = factory.SubFactory(CollectionFactory)
    language = factory.SubFactory(LanguageFactory)
