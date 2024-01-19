# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
SkosCollection factory to execute tests
"""

import factory
from ...models.skos_collection import SkosCollection


class SkosCollectionFactory(factory.django.DjangoModelFactory):
    """
    SkosCollection factory
    """

    class Meta:
        model = SkosCollection

    # FIXIT------------------
    number = factory.Faker('word')
    name = factory.Faker('word')
    uri = factory.Faker('url')
    type = "topic"
    collection = None
