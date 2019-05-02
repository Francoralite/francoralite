# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.collection_informer import (
        CollectionInformer as CollectionInformerModel)
from ..serializers.collection_informer import CollectionInformerSerializer


class CollectionInformerViewSet(viewsets.ModelViewSet):
    """
    CollectionInformer management
    """

    queryset = CollectionInformerModel.objects.all()
    serializer_class = CollectionInformerSerializer

    keycloak_scopes = {
        'GET': 'collection_informer:view',
        'POST': 'collection_informer:add',
        'PATCH': 'collection_informer:update',
        'PUT': 'collection_informer:update',
        'DELETE': 'collection_informer:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = CollectionInformerModel.objects.filter(
                collection_id=self.kwargs['collection_pk'])
        return queryset
