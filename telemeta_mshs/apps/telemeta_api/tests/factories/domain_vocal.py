# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
DomainVocal factory to execute tests
"""

import factory
from ...models.domain_vocal import DomainVocal


class DomainVocalFactory(factory.django.DjangoModelFactory):
    """
    DomainVocal factory
    """

    class Meta:
        model = DomainVocal

    name = factory.Sequence(lambda n: 'domain_v%d' % n)
    notes = factory.Faker('paragraph', nb_sentences=1)
