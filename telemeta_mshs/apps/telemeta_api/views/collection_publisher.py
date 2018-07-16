# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import viewsets
from ..models.collection_publisher import (
        CollectionPublisher as CollectionPublisherModel)
from ..serializers.collection_publisher import CollectionPublisherSerializer


class CollectionPublisherViewSet(viewsets.ModelViewSet):
    """
    CollectionPublisher management
    """

    queryset = CollectionPublisherModel.objects.all()
    serializer_class = CollectionPublisherSerializer
