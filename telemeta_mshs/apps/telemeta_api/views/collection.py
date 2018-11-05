# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from ..models.collection import Collection as CollectionModel
from ..serializers.collection import CollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    """
    Collection management
    """

    queryset = CollectionModel.objects.all()
    serializer_class = CollectionSerializer
