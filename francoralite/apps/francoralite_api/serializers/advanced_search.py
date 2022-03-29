# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel
from ..models.collection import Collection as CollectionModel
from ..models.collection_location import CollectionLocation as CollectionLocationModel
from ..models.coupe import Coupe as CoupeModel
from ..models.dance import Dance as DanceModel
from ..models.domain_song import DomainSong as DomainSongModel
from ..models.domain_music import DomainMusic as DomainMusicModel
from ..models.domain_tale import DomainTale as DomainTaleModel
from ..models.domain_vocal import DomainVocal as DomainVocalModel
from ..models.item import Item as ItemModel
from ..models.location import Location as LocationModel
from ..models.mediatype import MediaType as MediaTypeModel
from ..models.recording_context import RecordingContext as RecordingContextModel
from .authority import AuthoritySerializer
from .collection import CollectionSerializer
from .collection_location import CollectionLocationSerializer
from .coupe import CoupeSerializer
from .dance import DanceSerializer
from .domain_song import DomainSongSerializer
from .domain_music import DomainMusicSerializer
from .domain_tale import DomainTaleSerializer
from .domain_vocal import DomainVocalSerializer
from .item import ItemSerializer
from .location_gis import LocationGisSerializer
from .mediatype import MediaTypeSerializer
from .recording_context import RecordingContextSerializer


class AdvancedSearchSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if isinstance(instance, AuthorityModel):
            serializer = AuthoritySerializer(instance)
        elif isinstance(instance, CollectionModel):
            serializer = CollectionSerializer(instance)
        elif isinstance(instance, CollectionLocationModel):
            serializer = CollectionLocationSerializer(instance)
        elif isinstance(instance, CoupeModel):
            serializer = CoupeSerializer(instance)
        elif isinstance(instance, DanceModel):
            serializer = DanceSerializer(instance)
        elif isinstance(instance, DomainSongModel):
            serializer = DomainSongSerializer(instance)
        elif isinstance(instance, DomainMusicModel):
            serializer = DomainMusicSerializer(instance)
        elif isinstance(instance, DomainTaleModel):
            serializer = DomainTaleSerializer(instance)
        elif isinstance(instance, DomainVocalModel):
            serializer = DomainVocalSerializer(instance)
        elif isinstance(instance, ItemModel):
            serializer = ItemSerializer(instance)
        elif isinstance(instance, LocationModel):
            serializer = LocationGisSerializer(instance)
        elif isinstance(instance, MediaTypeModel):
            serializer = MediaTypeSerializer(instance)
        elif isinstance(instance, RecordingContextModel):
            serializer = RecordingContextSerializer(instance)
        else:
            raise Exception("Unknown instance type: %s" % type(instance))
        data = serializer.data
        data['entity'] = type(instance).__name__
        return data
