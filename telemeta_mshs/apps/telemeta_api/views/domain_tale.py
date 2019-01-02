# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.domain_tale import (
    DomainTale as DomainTaleModel)
from ..serializers.domain_tale import DomainTaleSerializer


class DomainTaleViewSet(viewsets.ModelViewSet):
    """
    DomainTale management
    """

    queryset = DomainTaleModel.objects.all()
    serializer_class = DomainTaleSerializer
