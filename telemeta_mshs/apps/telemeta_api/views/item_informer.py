# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_informer import (
        ItemInformer as ItemInformerModel)
from ..serializers.item_informer import ItemInformerSerializer


class ItemInformerViewSet(viewsets.ModelViewSet):
    """
    ItemInformer management
    """

    queryset = ItemInformerModel.objects.all()
    serializer_class = ItemInformerSerializer

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemInformerModel.objects.filter(
                item_id=self.kwargs['item_pk'])
            return queryset
