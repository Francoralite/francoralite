# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_dance import (
        ItemDance as ItemDanceModel)
from ..serializers.item_dance import ItemDanceSerializer


class ItemDanceViewSet(viewsets.ModelViewSet):
    """
    ItemDance management
    """

    queryset = ItemDanceModel.objects.all()
    serializer_class = ItemDanceSerializer

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemDanceModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
