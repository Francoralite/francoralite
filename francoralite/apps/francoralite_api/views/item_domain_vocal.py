# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_domain_vocal import (
        ItemDomainVocal as ItemDomainVocalModel)
from ..serializers.item_domain_vocal import ItemDomainVocalSerializer


class ItemDomainVocalViewSet(viewsets.ModelViewSet):
    """
    ItemDomainVocal management
    """

    queryset = ItemDomainVocalModel.objects.all()
    serializer_class = ItemDomainVocalSerializer

    keycloak_scopes = {
        'GET': 'item_domain_vocal:view',
        'POST': 'item_domain_vocal:add',
        'PATCH': 'item_domain_vocal:update',
        'PUT': 'item_domain_vocal:update',
        'DELETE': 'item_domain_vocal:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemDomainVocalModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
