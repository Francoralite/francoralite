# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Usefulness factory to execute tests
"""

import factory
from ...models.usefulness import Usefulness


class UsefulnessFactory(factory.django.DjangoModelFactory):
    """
    Usefulness factory
    """

    class Meta:
        model = Usefulness

    name = factory.Sequence(lambda n: 'usefulness%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
