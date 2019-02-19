# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_usefulness import (
        ItemUsefulness as ItemUsefulnessModel)
from ..serializers.item_usefulness import ItemUsefulnessSerializer


class ItemUsefulnessViewSet(viewsets.ModelViewSet):
    """
    ItemUsefulness management
    """

    queryset = ItemUsefulnessModel.objects.all()
    serializer_class = ItemUsefulnessSerializer

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemUsefulnessModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
