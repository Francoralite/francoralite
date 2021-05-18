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
from .acquisition_mode import AcquisitionModeFactory
from .institution import InstitutionFactory
from .mission import MissionFactory


class FondFactory(factory.django.DjangoModelFactory):
    """
    Fond factory
    """

    class Meta:
        model = Fond

    title = factory.Faker('word')
    alt_title = factory.Faker('word')
    description = factory.Faker('word')
    # descriptions = factory.Faker('word')
    code = factory.Faker('uuid4')
    institution = factory.SubFactory(InstitutionFactory)
    code_partner = factory.Faker('word')
    # public_access = factory.Iterator(['metadata', 'full'])
    acquisition_mode = factory.SubFactory(AcquisitionModeFactory)
    conservation_site = factory.Faker('word')
    comment = factory.Faker('word')


class FondFactoryMission(FondFactory):
    """
    Fond factory with missions
    """

    @factory.post_generation
    def missions( self, create, extracted, **kwargs):
        if not create: return
        nb_missions = kwargs.get('nb_missions',1)


        for n in range(nb_missions):
           MissionFactory(fonds = self)
