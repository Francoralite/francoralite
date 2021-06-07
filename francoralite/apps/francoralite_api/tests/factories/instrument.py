# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Instrument factory to execute tests
"""

import factory
from ...models.instrument import Instrument
from .hornbostelsachs import HornbostelSachsFactory


class InstrumentFactory(factory.django.DjangoModelFactory):
    """
    Instrument factory
    """

    class Meta:
        model = Instrument

    name = factory.Sequence(lambda n: 'instrument%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
    typology = factory.SubFactory(HornbostelSachsFactory)
