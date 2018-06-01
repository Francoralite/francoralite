# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from telemeta.models.collection import MediaCollection as MediacollectionModel
from ..serializers.MediaCollection import MediacollectionSerializer


class MediacollectionViewSet(viewsets.ModelViewSet):
    """
    Mediacollection management
    """

    queryset = MediacollectionModel.objects.all()
    serializer_class = MediacollectionSerializer
