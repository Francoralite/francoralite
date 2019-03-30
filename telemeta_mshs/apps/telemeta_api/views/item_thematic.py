# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_thematic import (
        ItemThematic as ItemThematicModel)
from ..serializers.item_thematic import ItemThematicSerializer


class ItemThematicViewSet(viewsets.ModelViewSet):
    """
    ItemThematic management
    """

    queryset = ItemThematicModel.objects.all()
    serializer_class = ItemThematicSerializer

    keycloak_scopes = {
        'GET': 'item_thematic:view',
        'POST': 'item_thematic:add',
        'PATCH': 'item_thematic:update',
        'PUT': 'item_thematic:update',
        'DELETE': 'item_thematic:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemThematicModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
