# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_musical_organization import (
        ItemMusicalOrganization as ItemMusicalOrganizationModel)
from ..serializers.item_musical_organization import (
    ItemMusicalOrganizationSerializer)


class ItemMusicalOrganizationViewSet(viewsets.ModelViewSet):
    """
    ItemMusicalOrganization management
    """

    queryset = ItemMusicalOrganizationModel.objects.all()
    serializer_class = ItemMusicalOrganizationSerializer

    keycloak_scopes = {
        'GET': 'item_musical_organization:view',
        'POST': 'item_musical_organization:add',
        'PATCH': 'item_musical_organization:update',
        'PUT': 'item_musical_organization:update',
        'DELETE': 'item_musical_organization:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemMusicalOrganizationModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
