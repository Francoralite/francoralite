# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.item_marker import ItemMarker as ItemMarkerModel
from ..models.item import Item as ItemModel
from ..serializers.item_marker import ItemMarkerSerializer
from jsonrpc import jsonrpc_method


class ItemMarkerViewSet(viewsets.ModelViewSet):
    """
    ItemMarker management
    """

    queryset = ItemMarkerModel.objects.all()
    serializer_class = ItemMarkerSerializer

    @jsonrpc_method('telemeta.get_markers')
    def get_markers(request, item_id):
        item = ItemModel.objects.get(id=item_id)
        markers = ItemMarkerModel.objects.filter(item=item)
        list = []
        for marker in markers:
            dict = {}
            dict['public_id'] = marker.public_id
            dict['time'] = str(marker.time)
            dict['title'] = marker.title
            dict['description'] = marker.description
            dict['author'] = marker.author.username
            list.append(dict)
        return list
