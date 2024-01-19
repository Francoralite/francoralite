# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Thematic factory to execute tests
"""

import factory
from ...models.thematic import Thematic


class ThematicFactory(factory.django.DjangoModelFactory):
    """
    Thematic factory
    """

    class Meta:
        model = Thematic

    name = factory.Sequence(lambda n: 'theme%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
