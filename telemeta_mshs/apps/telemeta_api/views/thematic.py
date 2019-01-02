# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.thematic import (
    Thematic as ThematicModel)
from ..serializers.thematic import ThematicSerializer


class ThematicViewSet(viewsets.ModelViewSet):
    """
    Thematic management
    """

    queryset = ThematicModel.objects.all()
    serializer_class = ThematicSerializer
