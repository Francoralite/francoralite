# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_language import (
    ItemLanguage as ItemLanguageModel)
from ..serializers.item_language import ItemLanguageSerializer


class ItemLanguageViewSet(viewsets.ModelViewSet):
    """
    ItemLanguage management
    """

    queryset = ItemLanguageModel.objects.all()
    serializer_class = ItemLanguageSerializer

    keycloak_scopes = {
        'GET': 'item_language:view',
        'POST': 'item_language:add',
        'PATCH': 'item_language:update',
        'PUT': 'item_language:update',
        'DELETE': 'item_language:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemLanguageModel.objects.filter(
                item_id=self.kwargs['item_pk'])
        return queryset
