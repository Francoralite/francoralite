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
from .item_informer import ItemInformer
from .item_author import ItemAuthor
from .item_compositor import ItemCompositor
from .item_domain_song import ItemDomainSong
from .item_domain_music import ItemDomainMusic
from .item_domain_vocal import ItemDomainVocal
from .item_domain_tale import ItemDomainTale
from .item_usefulness import ItemUsefulness
from .item_dance import ItemDance
from .item_thematic import ItemThematic
from .item_language import ItemLanguage
from .item_musical_organization import ItemMusicalOrganization
from .item_musical_group import ItemMusicalGroup
from .item_coirault import ItemCoirault
from .item_analysis import ItemAnalysis
from .item_transcoding_flag import ItemTranscodingFlag
from .item_marker import ItemMarker
from .collection import Collection
from .collectioncollectors import CollectionCollectors
from .collection_informer import CollectionInformer
from .collection_publisher import CollectionPublisher
from .collection_location import CollectionLocation
from .collection_language import CollectionLanguage
from .institution import Institution
from .language import Language
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
from .domain_tale import DomainTale
from .domain_music import DomainMusic
from .domain_vocal import DomainVocal
from .domain_song import DomainSong
from .usefulness import Usefulness
from .skos_collection import SkosCollection
from .skos_concept import SkosConcept
from .document import Document
from .document_fond import DocumentFond
from .document_mission import DocumentMission
from .document_collection import DocumentCollection
from .document_item import DocumentItem
