# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from ..models.item import Item as ItemModel
from ..serializers.item import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    Item management
    """
    parser_classes = (MultiPartParser,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
