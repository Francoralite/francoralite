# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.ext_media_item import ExtMediaItem as ExtMediaItemModel
from ..serializers.ext_media_item import ExtMediaItemSerializer


class ExtMediaItemViewSet(viewsets.ModelViewSet):
    """
    ExtMediaItem management
    """

    queryset = ExtMediaItemModel.objects.all()
    serializer_class = ExtMediaItemSerializer

    keycloak_scopes = {
        'GET': 'ext_media_item:view',
        'POST': 'ext_media_item:add',
        'PATCH': 'ext_media_item:update',
        'PUT': 'ext_media_item:update',
        'DELETE': 'ext_media_item:delete'
    }
