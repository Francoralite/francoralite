# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from ..models.collectioncollectors import (
    CollectionCollectors as CollectionCollectorsModel)
from ..serializers.collectioncollectors import CollectionCollectorsSerializer


class CollectionCollectorsViewSet(viewsets.ModelViewSet):
    """
    CollectionCollectors management
    """

    queryset = CollectionCollectorsModel.objects.all()
    serializer_class = CollectionCollectorsSerializer
