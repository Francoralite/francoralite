# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from ..models.ref_laforte import RefLaforte as RefLaforteModel
from ..serializers.ref_laforte import RefLaforteSerializer


class RefLaforteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Laforte to be viewed or edited.
    """
    queryset = RefLaforteModel.objects.all()
    serializer_class = RefLaforteSerializer

    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    ordering = ('name', 'number')
    search_fields = ('name', 'number')

    keycloak_scopes = {
        'GET': 'ref_laforte:view',
        'POST': 'ref_laforte:add',
        'PATCH': 'ref_laforte:update',
        'PUT': 'ref_laforte:update',
        'DELETE': 'ref_laforte:delete'
    }
