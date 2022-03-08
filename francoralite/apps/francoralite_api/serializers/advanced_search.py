# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.collection import Collection as CollectionModel
from ..models.collection_location import CollectionLocation as CollectionLocationModel
from ..models.item import Item as ItemModel
from .collection import CollectionSerializer
from .collection_location import CollectionLocationSerializer
from .item import ItemSerializer


class AdvancedSearchSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if isinstance(instance, CollectionModel):
            serializer = CollectionSerializer(instance)
        elif isinstance(instance, ItemModel):
            serializer = ItemSerializer(instance)
        elif isinstance(instance, CollectionLocationModel):
            serializer = CollectionLocationSerializer(instance)
        else:
            raise Exception("Unknown instance type: %s" % type(instance))
        data = serializer.data
        data['entity'] = type(instance).__name__
        return data
