# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

"""
location factory to execute tests
"""

import factory
from telemeta.models.location import Location
from .location_type import LocationTypeFactory


class LocationFactory(factory.django.DjangoModelFactory):
    """
    Location factory
    """

    class Meta:
        model = Location
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'Location {0}'.format(n))
    type = 0
    complete_type = factory.SubFactory(LocationTypeFactory)
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    is_authoritative = factory.Faker('boolean')
