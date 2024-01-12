# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Laforte factory to execute tests
"""

import factory
from ...models.ref_laforte import RefLaforte


class RefLaforteFactory(factory.django.DjangoModelFactory):
    """
    Laforte factory
    """

    class Meta:
        model = RefLaforte

    name = factory.Sequence(lambda n: 'laf%d' % n)
    description = factory.Faker('paragraph', nb_sentences=1)
