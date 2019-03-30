# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.dance import (
    Dance as DanceModel)
from ..serializers.dance import DanceSerializer


class DanceViewSet(viewsets.ModelViewSet):
    """
    Dance management
    """

    queryset = DanceModel.objects.all()
    serializer_class = DanceSerializer

    keycloak_scopes = {
        'GET': 'dance:view',
        'POST': 'dance:add',
        'PATCH': 'dance:update',
        'PUT': 'dance:update',
        'DELETE': 'dance:delete'
    }
