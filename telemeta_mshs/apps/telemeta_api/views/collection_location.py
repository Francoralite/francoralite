# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
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

    keycloak_scopes = {
        'GET': 'collection_location:view',
        'POST': 'collection_location:add',
        'PATCH': 'collection_location:update',
        'PUT': 'collection_location:update',
        'DELETE': 'collection_location:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = CollectionLocationModel.objects.filter(
                collection_id=self.kwargs['collection_pk'])
        return queryset
