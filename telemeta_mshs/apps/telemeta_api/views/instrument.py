# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from ..models.instrument import Instrument as InstrumentModel
from ..serializers.instrument import InstrumentSerializer


class InstrumentViewSet(viewsets.ModelViewSet):
    """
    Instrument management
    """

    queryset = InstrumentModel.objects.all()
    serializer_class = InstrumentSerializer

    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('name', 'typology')
    ordering = ('name', 'typology')
    search_fields = ('name', 'notes')

    keycloak_scopes = {
        'GET': 'instrument:view',
        'POST': 'instrument:add',
        'PATCH': 'instrument:update',
        'PUT': 'instrument:update',
        'DELETE': 'instrument:delete'
    }
