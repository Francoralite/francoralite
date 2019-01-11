# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_collector import (
        ItemCollector as ItemCollectorModel)
from ..serializers.item_collector import ItemCollectorSerializer


class ItemCollectorViewSet(viewsets.ModelViewSet):
    """
    ItemCollector management
    """

    queryset = ItemCollectorModel.objects.all()
    serializer_class = ItemCollectorSerializer

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemCollectorModel.objects.filter(
                item_id=self.kwargs['item_pk'])
        return queryset
