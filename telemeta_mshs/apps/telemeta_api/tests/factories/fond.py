# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Fond factory to execute tests
"""

import factory
from ...models.fond import Fond
from .acquistion_mode import AcquisitionModeFactory
from .institution import InstitutionFactory


class FondFactory(factory.django.DjangoModelFactory):
    """
    Fond factory
    """

    class Meta:
        model = Fond

    title = factory.Faker('word')
    description = factory.Faker('word')
    descriptions = factory.Faker('word')
    code = factory.Faker('uuid4')
    institution = factory.SubFactory(InstitutionFactory)
    public_access = factory.Iterator(['metadata', 'full'])
    acquisition_mode = factory.SubFactory(AcquisitionModeFactory)
    conservation_site = factory.Faker('word')
    comment = factory.Faker('word')
