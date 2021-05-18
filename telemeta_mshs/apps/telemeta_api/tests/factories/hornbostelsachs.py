# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
HornbostelSachs factory to execute tests
"""

import factory
from ...models.hornbostelsachs import HornbostelSachs


class HornbostelSachsFactory(factory.django.DjangoModelFactory):
    """
    HornbostelSachs factory
    """

    class Meta:
        model = HornbostelSachs

    number = factory.Sequence(lambda n: 'HB%d' % n)
    name = factory.Faker('paragraph', nb_sentences=1)
