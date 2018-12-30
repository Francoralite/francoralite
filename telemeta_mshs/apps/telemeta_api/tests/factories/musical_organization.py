# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
MusicalOrganization factory to execute tests
"""

import factory
from ...models.musical_organization import MusicalOrganization


class MusicalOrganizationFactory(factory.django.DjangoModelFactory):
    """
    MusicalOrganization factory
    """

    class Meta:
        model = MusicalOrganization

    name = factory.Faker('word')
    notes = factory.Faker('paragraph', nb_sentences=1)
