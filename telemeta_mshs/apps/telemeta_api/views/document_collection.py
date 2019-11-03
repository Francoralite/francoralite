# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.document_collection import (
    DocumentCollection as DocumentCollectionModel)
from ..serializers.document_collection import DocumentCollectionSerializer


class DocumentCollectionViewSet(viewsets.ModelViewSet):
    """
    DocumentCollection management
    """

    queryset = DocumentCollectionModel.objects.all()
    serializer_class = DocumentCollectionSerializer

    keycloak_scopes = {
        'GET': 'document_collection:view',
        'POST': 'document_collection:add',
        'PATCH': 'document_collection:update',
        'PUT': 'document_collection:update',
        'DELETE': 'document_collection:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = DocumentCollectionModel.objects.filter(
                collection_id=self.kwargs['collection_pk'])
        return queryset
