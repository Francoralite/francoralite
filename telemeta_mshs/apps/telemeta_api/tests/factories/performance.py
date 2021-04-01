# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Performance factory to execute tests
"""

import factory
from ...models.performance import Performance
from .instrument import InstrumentFactory
from .emit_vox import EmitVoxFactory


class PerformanceFactory(factory.django.DjangoModelFactory):
    """
    Performance factory
    """

    class Meta:
        model = Performance

    number = factory.Faker('pyint')
    instrument = factory.SubFactory(InstrumentFactory)
    emit = factory.SubFactory(EmitVoxFactory)
