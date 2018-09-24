# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from telemeta.models.item import MediaItem as MediaItemModel
from ..serializers.media_item import MediaItemSerializer


class MediaItemViewSet(viewsets.ModelViewSet):
    """
    MediaItem management
    """

    queryset = MediaItemModel.objects.all()
    serializer_class = MediaItemSerializer
