# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.document_mission import DocumentMission as DocumentMissionModel
from ..serializers.document_mission import DocumentMissionSerializer


class DocumentMissionViewSet(viewsets.ModelViewSet):
    """
    DocumentMission management
    """

    queryset = DocumentMissionModel.objects.all()
    serializer_class = DocumentMissionSerializer

    keycloak_scopes = {
        'GET': 'document_mission:view',
        'POST': 'document_mission:add',
        'PATCH': 'document_mission:update',
        'PUT': 'document_mission:update',
        'DELETE': 'document_mission:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = DocumentMissionModel.objects.filter(
                mission_id=self.kwargs['mission_pk'])
        return queryset
