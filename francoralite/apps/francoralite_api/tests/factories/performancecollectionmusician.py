# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:  2000  history | grep cookie / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
PerformanceCollectionMusician factory to execute tests
"""

import factory
from ...models.performance_collection_musician import PerformanceCollectionMusician
from .performancecollection import PerformanceCollectionFactory
from .authority import AuthorityFactory

class PerformanceCollectionMusicianFactory(factory.django.DjangoModelFactory):
    """
    PerformanceCollectionMusician factory
    """

    class Meta:
        model = PerformanceCollectionMusician
    
    performance_collection = factory.SubFactory(PerformanceCollectionFactory)
    musician = factory.SubFactory(AuthorityFactory)

