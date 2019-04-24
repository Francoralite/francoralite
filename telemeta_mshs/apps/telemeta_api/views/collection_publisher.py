# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
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

    keycloak_scopes = {
        'GET': 'collection_publisher:view',
        'POST': 'collection_publisher:add',
        'PATCH': 'collection_publisher:update',
        'PUT': 'collection_publisher:update',
        'DELETE': 'collection_publisher:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = CollectionPublisherModel.objects.filter(
                collection_id=self.kwargs['collection_pk'])
        return queryset
