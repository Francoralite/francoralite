# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.mediatype import MediaType as MediaTypeModel
from ..serializers.mediatype import MediaTypeSerializer


class MediaTypeViewSet(viewsets.ModelViewSet):
    """
    MediaType management
    """

    queryset = MediaTypeModel.objects.all()
    serializer_class = MediaTypeSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'mediatype:view',
        'POST': 'mediatype:add',
        'PATCH': 'mediatype:update',
        'PUT': 'mediatype:update',
        'DELETE': 'mediatype:delete',
    }
