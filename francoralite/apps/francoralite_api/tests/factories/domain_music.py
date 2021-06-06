# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
DomainMusic factory to execute tests
"""

import factory
from ...models.domain_music import DomainMusic


class DomainMusicFactory(factory.django.DjangoModelFactory):
    """
    DomainMusic factory
    """

    class Meta:
        model = DomainMusic

    name = factory.Sequence(lambda n: 'domain_m%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
