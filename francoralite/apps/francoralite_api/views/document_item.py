# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.document_item import (
    DocumentItem as DocumentItemModel)
from ..serializers.document_item import DocumentItemSerializer


class DocumentItemViewSet(viewsets.ModelViewSet):
    """
    DocumentItem management
    """

    queryset = DocumentItemModel.objects.all()
    serializer_class = DocumentItemSerializer

    keycloak_scopes = {
        'GET': 'document_item:view',
        'POST': 'document_item:add',
        'PATCH': 'document_item:update',
        'PUT': 'document_item:update',
        'DELETE': 'document_item:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = DocumentItemModel.objects.filter(
                item_id=self.kwargs['item_pk'])
        return queryset
