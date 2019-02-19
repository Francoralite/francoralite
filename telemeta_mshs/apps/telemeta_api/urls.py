from rest_framework_nested import routers
from .views import (
    authority,
    coupe,
    institution,
    fond,
    acquisition_mode,
    mission,
    collection,
    collectioncollectors,
    collection_informer,
    collection_publisher,
    collection_location,
    collection_language,
    location,
    location_gis,
    language,
    item,
    item_collector,
    item_informer,
    item_domain_song,
    item_domain_music,
    item_domain_vocal,
    item_domain_tale,
    item_usefulness,
    item_dance,
    item_thematic,
    item_musical_organization,
    mediatype,
    publisher,
    legal_rights,
    recording_context,
    emit_vox,
    hornbostelsachs,
    instrument,
    performance_collection,
    performance_collection_musician,
    musical_organization,
    musical_group,
    thematic,
    dance,
    domain_tale,
    domain_music,
    domain_vocal,
    domain_song,
    usefulness,
    )

router = routers.SimpleRouter()
router.register(r'institution',
                institution.InstitutionViewSet, base_name='institution')
router.register(r'coupe', coupe.CoupeViewSet, base_name='coupe')
router.register(r'mediatype',
                mediatype.MediaTypeViewSet, base_name='mediatype')
router.register(r'legalrights',
                legal_rights.LegalRightsViewSet, base_name='legal_rights')
router.register(r'recordingcontext',
                recording_context.RecordingContextViewSet,
                base_name='recordingcontext')
router.register(r'authority',
                authority.AuthorityViewSet, base_name='authority')
router.register(r'collection',
                collection.CollectionViewSet,
                base_name='collection')
router.register(r'location',
                location.LocationViewSet,
                base_name='location')
router.register(r'locationgis',
                location_gis.LocationGISViewSet,
                base_name='location_gis')
router.register(r'fond', fond.FondViewSet, base_name='fond'),
router.register(r'acquisitionmode',
                acquisition_mode.AcquisitionModeViewSet,
                base_name='acquisition_mode'),
router.register(r'mission', mission.MissionViewSet, base_name='mission'),
router.register(r'language',
                language.LanguageViewSet,
                base_name='language')
router.register(r'publisher',
                publisher.PublisherViewSet,
                base_name='publisher')
router.register(r'item',
                item.ItemViewSet,
                base_name='item')
router.register(r'emit_vox',
                emit_vox.EmitVoxViewSet,
                base_name='emit_vox')
router.register(r'hornbostelsachs',
                hornbostelsachs.HornbostelSachsViewSet,
                base_name='hornbostelsachs')
router.register(r'instrument',
                instrument.InstrumentViewSet,
                base_name='instrument')
router.register(r'musical_organization',
                musical_organization.MusicalOrganizationViewSet,
                base_name='musicalorganization')
router.register(r'musical_group',
                musical_group.MusicalGroupViewSet,
                base_name='musicalgroup')
router.register(r'thematic',
                thematic.ThematicViewSet,
                base_name='thematic')
router.register(r'dance',
                dance.DanceViewSet,
                base_name='dance')
router.register(r'domain_tale',
                domain_tale.DomainTaleViewSet,
                base_name='domaintale')
router.register(r'domain_music',
                domain_music.DomainMusicViewSet,
                base_name='domainmusic')
router.register(r'domain_vocal',
                domain_vocal.DomainVocalViewSet,
                base_name='domainvocal')
router.register(r'domain_song',
                domain_song.DomainSongViewSet,
                base_name='domainsong')
router.register(r'usefulness',
                usefulness.UsefulnessViewSet,
                base_name='usefulness')
# router.register(r'performance_collection_musician',
#                 performance_collection_musician.PerformanceCollectionMusicianViewSet,  # noqa
#                 base_name='performance_collection_musician')


# Nested routers
# Collection's nested ------------------------------------
Collection_router = routers.NestedSimpleRouter(
    router, r'collection', lookup='collection')
Collection_router.register(
    r'collectors', collectioncollectors.CollectionCollectorsViewSet)
Collection_router.register(
    r'informer', collection_informer.CollectionInformerViewSet)
Collection_router.register(
    r'publisher', collection_publisher.CollectionPublisherViewSet)
Collection_router.register(
    r'location', collection_location.CollectionLocationViewSet)
Collection_router.register(
    r'language', collection_language.CollectionLanguageViewSet)
Collection_router.register(
    r'performance', performance_collection.PerformanceCollectionViewSet)
Performance_router = routers.NestedSimpleRouter(
    Collection_router, r'performance', lookup='performance')
Performance_router.register(
    r'musician',
    performance_collection_musician.PerformanceCollectionMusicianViewSet)

# Item's nested ------------------------------------
Item_router = routers.NestedSimpleRouter(
     router, r'item', lookup='item')
Item_router.register(
    r'collector', item_collector.ItemCollectorViewSet)
Item_router.register(
    r'informer', item_informer.ItemInformerViewSet)
Item_router.register(
    r'domain_song', item_domain_song.ItemDomainSongViewSet)
Item_router.register(
    r'domain_music', item_domain_music.ItemDomainMusicViewSet)
Item_router.register(
    r'domain_vocal', item_domain_vocal.ItemDomainVocalViewSet)
Item_router.register(
    r'domain_tale', item_domain_tale.ItemDomainTaleViewSet)
Item_router.register(
    r'usefulness', item_usefulness.ItemUsefulnessViewSet)
Item_router.register(
    r'dance', item_dance.ItemDanceViewSet)
Item_router.register(
    r'thematic', item_thematic.ItemThematicViewSet)
Item_router.register(
    r'musical_organization',
    item_musical_organization.ItemMusicalOrganizationViewSet)
