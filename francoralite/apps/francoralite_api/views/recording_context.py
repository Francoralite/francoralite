# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.recording_context import RecordingContext as RecordingContextModel
from ..serializers.recording_context import RecordingContextSerializer


class RecordingContextViewSet(viewsets.ModelViewSet):
    """
    RecordingContext management
    """

    queryset = RecordingContextModel.objects.all()
    serializer_class = RecordingContextSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'recording_context:view',
        'POST': 'recording_context:add',
        'PATCH': 'recording_context:update',
        'PUT': 'recording_context:update',
        'DELETE': 'recording_context:delete',
    }
