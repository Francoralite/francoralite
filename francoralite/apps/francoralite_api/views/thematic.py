# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.thematic import Thematic as ThematicModel
from ..serializers.thematic import ThematicSerializer


class ThematicViewSet(viewsets.ModelViewSet):
    """
    Thematic management
    """

    queryset = ThematicModel.objects.all()
    serializer_class = ThematicSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'thematic:view',
        'POST': 'thematic:add',
        'PATCH': 'thematic:update',
        'PUT': 'thematic:update',
        'DELETE': 'thematic:delete',
    }
