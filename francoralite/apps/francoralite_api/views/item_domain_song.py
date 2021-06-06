# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_domain_song import (
        ItemDomainSong as ItemDomainSongModel)
from ..serializers.item_domain_song import ItemDomainSongSerializer


class ItemDomainSongViewSet(viewsets.ModelViewSet):
    """
    ItemDomainSong management
    """

    queryset = ItemDomainSongModel.objects.all()
    serializer_class = ItemDomainSongSerializer

    keycloak_scopes = {
        'GET': 'item_domain_song:view',
        'POST': 'item_domain_song:add',
        'PATCH': 'item_domain_song:update',
        'PUT': 'item_domain_song:update',
        'DELETE': 'item_domain_song:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemDomainSongModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
