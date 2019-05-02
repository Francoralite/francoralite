# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_domain_music import (
        ItemDomainMusic as ItemDomainMusicModel)
from ..serializers.item_domain_music import ItemDomainMusicSerializer


class ItemDomainMusicViewSet(viewsets.ModelViewSet):
    """
    ItemDomainMusic management
    """

    queryset = ItemDomainMusicModel.objects.all()
    serializer_class = ItemDomainMusicSerializer

    keycloak_scopes = {
        'GET': 'item_domain_music:view',
        'POST': 'item_domain_music:add',
        'PATCH': 'item_domain_music:update',
        'PUT': 'item_domain_music:update',
        'DELETE': 'item_domain_music:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemDomainMusicModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
