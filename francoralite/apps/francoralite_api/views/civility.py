# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.civility import Civility as CivilityModel
from ..serializers.civility import CivilitySerializer


class CivilityViewSet(viewsets.ModelViewSet):
    """
    Civility management
    """

    queryset = CivilityModel.objects.all()
    serializer_class = CivilitySerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'civility:view',
        'POST': 'civility:add',
        'PATCH': 'civility:update',
        'PUT': 'civility:update',
        'DELETE': 'civility:delete',
    }
