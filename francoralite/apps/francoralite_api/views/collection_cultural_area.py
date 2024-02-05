# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.collection_cultural_area import CollectionCulturalArea as CollectionCulturalAreaModel
from ..serializers.collection_cultural_area import CollectionCulturalAreaSerializer


class CollectionCulturalAreaViewSet(viewsets.ModelViewSet):
    """
    CollectionCulturalArea management
    """

    queryset = CollectionCulturalAreaModel.objects.all()
    serializer_class = CollectionCulturalAreaSerializer

    keycloak_scopes = {
        'GET': 'collection_cultural_area:view',
        'POST': 'collection_cultural_area:add',
        'PATCH': 'collection_cultural_area:update',
        'PUT': 'collection_cultural_area:update',
        'DELETE': 'collection_cultural_area:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = CollectionCulturalAreaModel.objects.filter(
                collection_id=self.kwargs['collection_pk'])
        return queryset
