# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from ..models.emit_vox import EmitVox as EmitVoxModel
from ..serializers.emit_vox import EmitVoxSerializer


class EmitVoxViewSet(viewsets.ModelViewSet):
    """
    Vocal emission management
    """

    queryset = EmitVoxModel.objects.all()
    serializer_class = EmitVoxSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ()
    ordering = ('name')
    search_fields = ('name')

    keycloak_scopes = {
        'GET': 'emit_vox:view',
        'POST': 'emit_vox:add',
        'PATCH': 'emit_vox:update',
        'PUT': 'emit_vox:update',
        'DELETE': 'emit_vox:delete'
    }
