# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.fond import Fond as FondModel
from ..serializers.fond import FondSerializer


class FondViewSet(viewsets.ModelViewSet):
    """
    Fond management
    """

    queryset = FondModel.objects.all()
    serializer_class = FondSerializer
