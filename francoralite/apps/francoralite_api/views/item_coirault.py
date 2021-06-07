# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_coirault import (
        ItemCoirault as ItemCoiraultModel)
from ..serializers.item_coirault import ItemCoiraultSerializer


class ItemCoiraultViewSet(viewsets.ModelViewSet):
    """
    ItemCoirault management
    """

    queryset = ItemCoiraultModel.objects.all()
    serializer_class = ItemCoiraultSerializer

    keycloak_scopes = {
        'GET': 'item_coirault:view',
        'POST': 'item_coirault:add',
        'PATCH': 'item_coirault:update',
        'PUT': 'item_coirault:update',
        'DELETE': 'item_coirault:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemCoiraultModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
