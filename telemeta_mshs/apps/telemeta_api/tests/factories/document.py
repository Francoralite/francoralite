# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
document factory to execute tests
"""

import factory
from ...models.document import Document

class DocumentFactory(factory.django.DjangoModelFactory):
    """
    Document factory
    """

    class Meta:
        model = Document

    id_nakala = factory.Faker('word')
    title = factory.Faker('word')
    description = factory.Faker('paragraph', nb_sentences=3)
    credits = factory.Faker('paragraph', nb_sentences=3)
    date = factory.Faker('date')
