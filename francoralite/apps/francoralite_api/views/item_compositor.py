# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_compositor import (
        ItemCompositor as ItemCompositorModel)
from ..serializers.item_compositor import ItemCompositorSerializer


class ItemCompositorViewSet(viewsets.ModelViewSet):
    """
    ItemCompositor management
    """

    queryset = ItemCompositorModel.objects.all()
    serializer_class = ItemCompositorSerializer

    keycloak_scopes = {
        'GET': 'item_compositor:view',
        'POST': 'item_compositor:add',
        'PATCH': 'item_compositor:update',
        'PUT': 'item_compositor:update',
        'DELETE': 'item_compositor:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            # FIXIT ---------------------
            queryset = ItemCompositorModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
