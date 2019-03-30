# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.item_marker import ItemMarker as ItemMarkerModel
from ..serializers.item_marker import ItemMarkerSerializer


class ItemMarkerViewSet(viewsets.ModelViewSet):
    """
    ItemMarker management
    """

    queryset = ItemMarkerModel.objects.all()
    serializer_class = ItemMarkerSerializer

    keycloak_scopes = {
        'GET': 'item_marker:view',
        'POST': 'item_marker:add',
        'PATCH': 'item_marker:update',
        'PUT': 'item_marker:update',
        'DELETE': 'item_marker:delete'
    }
