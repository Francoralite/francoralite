# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_musical_group import (
        ItemMusicalGroup as ItemMusicalGroupModel)
from ..serializers.item_musical_group import ItemMusicalGroupSerializer


class ItemMusicalGroupViewSet(viewsets.ModelViewSet):
    """
    ItemMusicalGroup management
    """

    queryset = ItemMusicalGroupModel.objects.all()
    serializer_class = ItemMusicalGroupSerializer

    keycloak_scopes = {
        'GET': 'item_musical_group:view',
        'POST': 'item_musical_group:add',
        'PATCH': 'item_musical_group:update',
        'PUT': 'item_musical_group:update',
        'DELETE': 'item_musical_group:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemMusicalGroupModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
