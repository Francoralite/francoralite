# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
SkosConcept factory to execute tests
"""

import factory
from ...models.skos_concept import SkosConcept
from .skos_collection import SkosCollectionFactory


class SkosConceptFactory(factory.django.DjangoModelFactory):
    """
    SkosConcept factory
    """

    class Meta:
        model = SkosConcept

    name = factory.Faker('word')
    uri = factory.Faker('url')
    number = factory.Faker('word')
    abstract = factory.Faker('word')
    collection = factory.SubFactory(SkosCollectionFactory)
