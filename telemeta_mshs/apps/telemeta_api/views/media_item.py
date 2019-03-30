# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from telemeta.models.item import MediaItem as MediaItemModel
from ..serializers.media_item import MediaItemSerializer


class MediaItemViewSet(viewsets.ModelViewSet):
    """
    MediaItem management
    """

    queryset = MediaItemModel.objects.all()
    serializer_class = MediaItemSerializer

    keycloak_scopes = {
        'GET': 'media_item:view',
        'POST': 'media_item:add',
        'PATCH': 'media_item:update',
        'PUT': 'media_item:update',
        'DELETE': 'media_item:delete'
    }
