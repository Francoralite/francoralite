# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.publisher import Publisher as PublisherModel
from ..serializers.publisher import PublisherSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    Publisher management
    """

    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

    keycloak_scopes = {
        'GET': 'publisher:view',
        'POST': 'publisher:add',
        'PATCH': 'publisher:update',
        'PUT': 'publisher:update',
        'DELETE': 'publisher:delete'
    }
