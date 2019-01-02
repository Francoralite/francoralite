# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.item_function import (
    ItemFunction as ItemFunctionModel)
from ..serializers.item_function import ItemFunctionSerializer


class ItemFunctionViewSet(viewsets.ModelViewSet):
    """
    ItemFunction management
    """

    queryset = ItemFunctionModel.objects.all()
    serializer_class = ItemFunctionSerializer
