# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import viewsets
from ..models.collection_location import (
        CollectionLocation as CollectionLocationModel)
from ..serializers.collection_location import CollectionLocationSerializer


class CollectionLocationViewSet(viewsets.ModelViewSet):
    """
    CollectionLocation management
    """

    queryset = CollectionLocationModel.objects.all()
    serializer_class = CollectionLocationSerializer
