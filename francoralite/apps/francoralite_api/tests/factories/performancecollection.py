# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
PerformanceCollection factory to execute tests
"""

import factory
from ...models.performance_collection import PerformanceCollection
from .instrument import InstrumentFactory
from .emit_vox import EmitVoxFactory


class PerformanceCollectionFactory(factory.django.DjangoModelFactory):
    """
    PerformanceCollection factory
    """

    class Meta:
        model = PerformanceCollection
    
    collection = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.collection.CollectionFactory")
    number = factory.Faker('pyint')
    instrument = factory.SubFactory(InstrumentFactory)
    emit = factory.SubFactory(EmitVoxFactory)
