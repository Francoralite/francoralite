# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.musical_group import (
    MusicalGroup as MusicalGroupModel)
from ..serializers.musical_group import MusicalGroupSerializer


class MusicalGroupViewSet(viewsets.ModelViewSet):
    """
    MusicalGroup management
    """

    queryset = MusicalGroupModel.objects.all()
    serializer_class = MusicalGroupSerializer
