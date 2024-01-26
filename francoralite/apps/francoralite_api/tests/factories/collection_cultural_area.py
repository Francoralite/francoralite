# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
CollectionCulturalArea factory to execute tests
"""

import factory
from ...models.collection_cultural_area import CollectionCulturalArea
# Import nested/related factories
from .cultural_area import CulturalAreaFactory


class CollectionCulturalAreaFactory(factory.django.DjangoModelFactory):
    """
    CollectionCulturalArea factory
    """

    class Meta:
        model = CollectionCulturalArea
        django_get_or_create = (
            'collection',
            'cultural_area',)

    # Nested/related factories
    collection = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.collection.CollectionItemsFactory")
    cultural_area = factory.SubFactory(CulturalAreaFactory)
