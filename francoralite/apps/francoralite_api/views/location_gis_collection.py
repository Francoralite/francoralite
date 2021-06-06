# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import generics

from ..models.collection_location import CollectionLocation
from ..serializers.collection_location import CollectionLocationSerializer


class LocationGisCollectionList(generics.ListAPIView):
    serializer_class = CollectionLocationSerializer

    def get_queryset(self):
        collections = CollectionLocation.objects.all()
        return collections
