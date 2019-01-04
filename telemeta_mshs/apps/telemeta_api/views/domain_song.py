# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.domain_song import (
    DomainSong as DomainSongModel)
from ..serializers.domain_song import DomainSongSerializer


class DomainSongViewSet(viewsets.ModelViewSet):
    """
    DomainSong management
    """

    queryset = DomainSongModel.objects.all()
    serializer_class = DomainSongSerializer
