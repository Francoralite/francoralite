# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Keyword factory to execute tests
"""

import factory
from ...models.keyword import Keyword


class KeywordFactory(factory.django.DjangoModelFactory):
    """
    Keyword factory
    """

    class Meta:
        model = Keyword

    name = factory.Sequence(lambda n: 'theme%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
