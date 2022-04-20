# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.coupe import Coupe as CoupeModel
from ..serializers.coupe import CoupeSerializer


class CoupeViewSet(viewsets.ModelViewSet):
    """
    Coupe management
    """

    queryset = CoupeModel.objects.all()
    serializer_class = CoupeSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'coupe:view',
        'POST': 'coupe:add',
        'PATCH': 'coupe:update',
        'PUT': 'coupe:update',
        'DELETE': 'coupe:delete',
    }
