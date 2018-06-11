# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from ..models.ext_media_collection import (
    ExtMediaCollection as ExtMediaCollectionModel)
from ..serializers.ext_media_collection import ExtMediacollectionSerializer


class ExtMediacollectionViewSet(viewsets.ModelViewSet):
    """
    Mediacollection management
    """

    queryset = ExtMediaCollectionModel.objects.all()
    serializer_class = ExtMediacollectionSerializer
