# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from ..models.skos_collection import SkosCollection as SkosCollectionModel
from ..serializers.skos_collection import SkosCollectionSerializer


class SkosCollectionViewSet(viewsets.ModelViewSet):
    """
    SkosCollection management
    """

    queryset = SkosCollectionModel.objects.all()
    serializer_class = SkosCollectionSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('parent', 'type')
    ordering = ('name', 'number', 'parent', 'type')
    search_fields = ('name', 'number', 'uri')

    keycloak_scopes = {
        'GET': 'fond:view',
    }
