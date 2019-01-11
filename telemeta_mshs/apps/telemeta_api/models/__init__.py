"""
Manage these import to have models discoverables from Django makemigrations
"""

from .authority import Authority
from .coupe import Coupe
from .mediatype import MediaType
from .legal_rights import LegalRights
from .metadata_author import MetadataAuthor
from .publisher import Publisher
from .recording_context import RecordingContext
from .ext_media_item import ExtMediaItem
from .item import Item
from .item_collector import ItemCollector
from .collection import Collection
from .collectioncollectors import CollectionCollectors
from .collection_informer import CollectionInformer
from .collection_publisher import CollectionPublisher
from .collection_location import CollectionLocation
from .collection_language import CollectionLanguage
from .institution import Institution
from .location import Location
from .fond import Fond
from .acquisition_mode import AcquisitionMode
from .mission import Mission
from .emit_vox import EmitVox
from .hornbostelsachs import HornbostelSachs
from .instrument import Instrument
from .performance_collection_musician import PerformanceCollectionMusician
from .performance_collection import PerformanceCollection
from .musical_organization import MusicalOrganization
from .musical_group import MusicalGroup
from .thematic import Thematic
from .dance import Dance
from .item_function import ItemFunction
from .domain_tale import DomainTale
from .domain_music import DomainMusic
from .domain_vocal import DomainVocal
from .domain_song import DomainSong
