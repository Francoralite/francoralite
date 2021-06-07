# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.document_fond import DocumentFond as DocumentFondModel
from ..serializers.document_fond import DocumentFondSerializer


class DocumentFondViewSet(viewsets.ModelViewSet):
    """
    DocumentFond management
    """

    queryset = DocumentFondModel.objects.all()
    serializer_class = DocumentFondSerializer

    keycloak_scopes = {
        'GET': 'document_fond:view',
        'POST': 'document_fond:add',
        'PATCH': 'document_fond:update',
        'PUT': 'document_fond:update',
        'DELETE': 'document_fond:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = DocumentFondModel.objects.filter(
                fond_id=self.kwargs['fond_pk'])
        return queryset
