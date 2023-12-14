# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_keyword import (
        ItemKeyword as ItemKeywordModel)
from ..serializers.item_keyword import ItemKeywordSerializer


class ItemKeywordViewSet(viewsets.ModelViewSet):
    """
    ItemKeyword management
    """

    queryset = ItemKeywordModel.objects.all()
    serializer_class = ItemKeywordSerializer

    keycloak_scopes = {
        'GET': 'item_keyword:view',
        'POST': 'item_keyword:add',
        'PATCH': 'item_keyword:update',
        'PUT': 'item_keyword:update',
        'DELETE': 'item_keyword:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemKeywordModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
