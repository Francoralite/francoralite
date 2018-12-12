# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from ..models.instrument import Instrument as InstrumentModel
from ..serializers.instrument import InstrumentSerializer


class InstrumentViewSet(viewsets.ModelViewSet):
    """
    Instrument management
    """

    queryset = InstrumentModel.objects.all()
    serializer_class = InstrumentSerializer

    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'typology')
    ordering = ('name', 'typology')
    search_fields = ('name', 'notes')
