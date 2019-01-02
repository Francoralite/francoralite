# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.domain_music import (
    DomainMusic as DomainMusicModel)
from ..serializers.domain_music import DomainMusicSerializer


class DomainMusicViewSet(viewsets.ModelViewSet):
    """
    DomainMusic management
    """

    queryset = DomainMusicModel.objects.all()
    serializer_class = DomainMusicSerializer
