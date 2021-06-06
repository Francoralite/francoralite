# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel
from .authority import AuthoritySerializer
from ..models.location import Location as LocationModel
from .location_gis import LocationGisSerializer
from ..models.fond import Fond as FondModel
from .fond import FondSerializer
from ..models.mission import Mission as MissionModel
from .mission import MissionSerializer
from ..models.collection import Collection as CollectionModel
from .collection import CollectionSerializer
from ..models.item import Item as ItemModel
from .item import ItemSerializer


class AdvancedSearchSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if isinstance(instance, AuthorityModel):
            serializer = AuthoritySerializer(instance)
        elif isinstance(instance, LocationModel):
            serializer = LocationGisSerializer(instance)
        elif isinstance(instance, FondModel):
            serializer = FondSerializer(instance)
        elif isinstance(instance, MissionModel):
            serializer = MissionSerializer(instance)
        elif isinstance(instance, CollectionModel):
            serializer = CollectionSerializer(instance)
        elif isinstance(instance, ItemModel):
            serializer = ItemSerializer(instance)
        else:
            raise Exception("Not an known instance!")
        data = serializer.data
        data['entity'] = type(instance).__name__
        return data
