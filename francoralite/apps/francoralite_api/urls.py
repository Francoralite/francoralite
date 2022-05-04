from rest_framework_nested import routers
from django.conf.urls import re_path
from .views import (
    authority,
    coupe,
    institution,
    fond,
    document_fond,
    acquisition_mode,
    mission,
    document_mission,
    civility,
    code_external,
    code_internal,
    collection,
    document_collection,
    collectioncollectors,
    collection_informer,
    collection_publisher,
    collection_location,
    collection_language,
    cultural_area,
    location_gis,
    location_gis_collection,
    language,
    item,
    document_item,
    item_collector,
    item_informer,
    item_author,
    item_compositor,
    item_domain_song,
    item_domain_music,
    item_domain_vocal,
    item_domain_tale,
    item_usefulness,
    item_dance,
    item_language,
    item_thematic,
    item_coirault,
    item_musical_organization,
    item_musical_group,
    item_performance,
    mediatype,
    metadata_author,
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
    versions,
    global_search,
    advanced_search,
    skos_collection,
    skos_concept,
    timbre,
    timbre_ref,
)

urlpatterns = [
    re_path(r'^versions/$',versions.VersionsView.as_view(), name="versions" ),
    re_path(r'^globalsearch/$', global_search.GlobalSearchList.as_view(),
        name="search"),
    re_path(r'^advancedsearch/$', advanced_search.AdvancedSearchList.as_view(),
        name="search_advanced"),
    re_path(r'^api/locationgiscollection/$',
        location_gis_collection.LocationGisCollectionList.as_view(),
        name="location_gis_collection"),
    re_path(r'^api/civility/$', civility.CivilityView.as_view(),
        name="civility"),
    re_path(r'^api/code_external/$', code_external.CodeExternalView.as_view(),
        name="code_external"),
    re_path(r'^api/code_internal/$', code_internal.CodeInternalView.as_view(),
        name="code_internal"),
    re_path(r'^api/cultural_area/$', cultural_area.CulturalAreaView.as_view(),
        name="cultural_area"),
    re_path(r'^api/timbre/$', timbre.TimbreView.as_view(),
        name="timbre"),
    re_path(r'^api/timbre_ref/$', timbre_ref.TimbreRefView.as_view(),
        name="timbre_ref"),
]

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'institution',
                institution.InstitutionViewSet, basename='institution')
router.register(r'coupe', coupe.CoupeViewSet, basename='coupe')
router.register(r'mediatype',
                mediatype.MediaTypeViewSet, basename='mediatype')
router.register(r'metadata_author',
                metadata_author.MetadataAuthorViewSet,
                basename='metadata_author')
router.register(r'legalrights',
                legal_rights.LegalRightsViewSet, basename='legal_rights')
router.register(r'recordingcontext',
                recording_context.RecordingContextViewSet,
                basename='recordingcontext')
router.register(r'authority',
                authority.AuthorityViewSet, basename='authority')
router.register(r'collection',
                collection.CollectionViewSet,
                basename='collection')
router.register(r'locationgis',
                location_gis.LocationGISViewSet,
                basename='location_gis')
# router.register(r'locationgiscollection',
#                 location_gis_collection.LocationGisCollectionList,
#                 basename='location_gis_collection')
router.register(r'fond', fond.FondViewSet, basename='fond'),
router.register(r'acquisitionmode',
                acquisition_mode.AcquisitionModeViewSet,
                basename='acquisition_mode'),
router.register(r'mission', mission.MissionViewSet, basename='mission'),
router.register(r'language',
                language.LanguageViewSet,
                basename='language')
router.register(r'publisher',
                publisher.PublisherViewSet,
                basename='publisher')
router.register(r'item',
                item.ItemViewSet,
                basename='item')
router.register(r'emit_vox',
                emit_vox.EmitVoxViewSet,
                basename='emit_vox')
router.register(r'hornbostelsachs',
                hornbostelsachs.HornbostelSachsViewSet,
                basename='hornbostelsachs')
router.register(r'instrument',
                instrument.InstrumentViewSet,
                basename='instrument')
router.register(r'musical_organization',
                musical_organization.MusicalOrganizationViewSet,
                basename='musicalorganization')
router.register(r'musical_group',
                musical_group.MusicalGroupViewSet,
                basename='musicalgroup')
router.register(r'thematic',
                thematic.ThematicViewSet,
                basename='thematic')
router.register(r'dance',
                dance.DanceViewSet,
                basename='dance')
router.register(r'domain_tale',
                domain_tale.DomainTaleViewSet,
                basename='domaintale')
router.register(r'domain_music',
                domain_music.DomainMusicViewSet,
                basename='domainmusic')
router.register(r'domain_vocal',
                domain_vocal.DomainVocalViewSet,
                basename='domainvocal')
router.register(r'domain_song',
                domain_song.DomainSongViewSet,
                basename='domainsong')
router.register(r'usefulness',
                usefulness.UsefulnessViewSet,
                basename='usefulness')
# router.register(r'performance_collection_musician',
#                 performance_collection_musician.PerformanceCollectionMusicianViewSet,  # noqa
#                 basename='performance_collection_musician')

router.register(r'skos_collection',
                skos_collection.SkosCollectionViewSet,
                basename='coirault')
router.register(r'skos_concept',
                skos_concept.SkosConceptViewSet,
                basename='coirault')

# Nested routers

# Fond's nested ------------------------------------
Fond_router = routers.NestedSimpleRouter(
    router, r'fond', lookup='fond', trailing_slash=False)
Fond_router.register(
    r'document', document_fond.DocumentFondViewSet)

# Mission's nested ------------------------------------
Mission_router = routers.NestedSimpleRouter(
    router, r'mission', lookup='mission', trailing_slash=False)
Mission_router.register(
    r'document', document_mission.DocumentMissionViewSet)

# Collection's nested ------------------------------------
Collection_router = routers.NestedSimpleRouter(
    router, r'collection', lookup='collection', trailing_slash=False)
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
    Collection_router, r'performance', lookup='performance',
    trailing_slash=False)
Performance_router.register(
    r'musician',
    performance_collection_musician.PerformanceCollectionMusicianViewSet)
Collection_router.register(
    r'document', document_collection.DocumentCollectionViewSet)

# Item's nested ------------------------------------
Item_router = routers.NestedSimpleRouter(
     router, r'item', lookup='item', trailing_slash=False)
Item_router.register(
    r'collector', item_collector.ItemCollectorViewSet)
Item_router.register(
    r'informer', item_informer.ItemInformerViewSet)
Item_router.register(
    r'author', item_author.ItemAuthorViewSet)
Item_router.register(
    r'compositor', item_compositor.ItemCompositorViewSet)
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
    r'language', item_language.ItemLanguageViewSet)
Item_router.register(
    r'thematic', item_thematic.ItemThematicViewSet)
Item_router.register(
    r'musical_organization',
    item_musical_organization.ItemMusicalOrganizationViewSet)
Item_router.register(
    r'coirault', item_coirault.ItemCoiraultViewSet
)
Item_router.register(
    r'document', document_item.DocumentItemViewSet)
Item_router.register(
    r'musical_group',
    item_musical_group.ItemMusicalGroupViewSet)
Item_router.register(
    r'performance', item_performance.ItemPerformanceViewSet)
