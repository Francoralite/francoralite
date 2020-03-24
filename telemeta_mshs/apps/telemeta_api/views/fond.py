# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from ..models.fond import Fond as FondModel
from ..serializers.fond import FondSerializer


class FondViewSet(viewsets.ModelViewSet):
    """
    Fond management
    """

    queryset = FondModel.objects.all()
    serializer_class = FondSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('institution',)
    # ordering = ('institution', 'code',)
    # search_fields = ('institution__name', 'code', 'title')
    filter_fields = ('code', 'title')

    keycloak_scopes = {
        'GET': 'fond:view',
        'POST': 'fond:add',
        'PATCH': 'fond:update',
        'PUT': 'fond:update',
        'DELETE': 'fond:delete'
    }
