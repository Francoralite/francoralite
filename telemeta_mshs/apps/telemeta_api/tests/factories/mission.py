# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Mission factory to execute tests
"""

import factory
from ...models.mission import Mission


class MissionFactory(factory.django.DjangoModelFactory):
    """
    Mission factory
    """

    class Meta:
        model = Mission

    title = factory.Faker('word')
    description = factory.Faker('word')
    # descriptions = factory.Faker('word')
    code = factory.Faker('uuid4')
    fonds = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.fond.FondFactory")
    code_partner = factory.Faker('word')
    public_access = factory.Iterator(['metadata', 'full'])
