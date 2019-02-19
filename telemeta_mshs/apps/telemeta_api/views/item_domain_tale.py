# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_domain_tale import (
        ItemDomainTale as ItemDomainTaleModel)
from ..serializers.item_domain_tale import ItemDomainTaleSerializer


class ItemDomainTaleViewSet(viewsets.ModelViewSet):
    """
    ItemDomainTale management
    """

    queryset = ItemDomainTaleModel.objects.all()
    serializer_class = ItemDomainTaleSerializer

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemDomainTaleModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
