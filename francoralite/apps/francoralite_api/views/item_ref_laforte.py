# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.item_laforte import (
    ItemLaforte as ItemLaforteModel
)
from ..serializers.item_laforte import (
    ItemLaforteSerializer
)


class ItemRefLaforteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows item_ref_laforte to be viewed or edited.
    """
    queryset = ItemLaforteModel.objects.all()
    serializer_class = ItemLaforteSerializer
    
    keycloak_scopes = {
        'GET': 'item_ref_laforte:view',
        'POST': 'item_ref_laforte:add',
        'PATCH': 'item_ref_laforte:update',
        'PUT': 'item_ref_laforte:update',
        'DELETE': 'item_ref_laforte:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = ItemLaforteModel.objects.filter(
               item_id=self.kwargs['item_pk'])
        return queryset
