# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
collection_location factory to execute tests
"""

import factory
from ...models.collection_location import CollectionLocation
# Import nested/related factories
from .location_gis import LocationGisFactory


class CollectionLocationFactory(factory.django.DjangoModelFactory):
    """
    CollectionLocation factory
    """

    class Meta:
        model = CollectionLocation
        django_get_or_create = (
            'collection',
            'location',)

    # Nested/related factories
    collection = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.collection.CollectionFactory")
    location = factory.SubFactory(LocationGisFactory)
