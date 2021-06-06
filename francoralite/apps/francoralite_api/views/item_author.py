# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_author import (
        ItemAuthor as ItemAuthorModel)
from ..serializers.item_author import ItemAuthorSerializer


class ItemAuthorViewSet(viewsets.ModelViewSet):
    """
    ItemAuthor management
    """

    queryset = ItemAuthorModel.objects.all()
    serializer_class = ItemAuthorSerializer

    keycloak_scopes = {
        'GET': 'item_author:view',
        'POST': 'item_author:add',
        'PATCH': 'item_author:update',
        'PUT': 'item_author:update',
        'DELETE': 'item_author:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemAuthorModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
