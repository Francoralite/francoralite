from rest_framework_nested import routers
from django.conf.urls import re_path
from .views import (
    acquisition_mode,
    advanced_search,
    authority,
    authority_civility,
    block,
    civility,
    code_external,
    code_internal,
    collection,
    collection_cultural_area,
    collection_informer,
    collection_language,
    collection_location,
    collection_publisher,
    collectioncollectors,
    coupe,
    cultural_area,
    dance,
    document_collection,
    document_fond,
    document_item,
    document_mission,
    domain_music,
    domain_song,
    domain_tale,
    domain_vocal,
    emit_vox,
    fond,
    global_search,
    hornbostelsachs,
    institution,
    instrument,
    item,
    item_author,
    item_coirault,
    item_collector,
    item_compositor,
    item_dance,
    item_domain_music,
    item_domain_song,
    item_domain_tale,
    item_domain_vocal,
    item_informer,
    item_keyword,
    item_language,
    item_ref_laforte,
    item_musical_group,
    item_musical_organization,
    item_performance,
    item_thematic,
    item_usefulness,
    keyword,
    language,
    legal_rights,
    location_gis,
    location_gis_collection,
    mediatype,
    metadata_author,
    mission,
    musical_group,
    musical_organization,
    performance_collection,
    performance_collection_musician,
    publisher,
    recording_context,
    ref_laforte,
    skos_collection,
    skos_concept,
    thematic,
    timbre,
    timbre_ref,
    usefulness,
    versions,
)


urlpatterns = [
    re_path(r'^advancedsearch/$', advanced_search.AdvancedSearchList.as_view(),
        name='search_advanced'),
    re_path(r'^api/code_external/$', code_external.CodeExternalView.as_view(),
        name='code_external'),
    re_path(r'^api/code_internal/$', code_internal.CodeInternalView.as_view(),
        name='code_internal'),
    re_path(r'^api/locationgiscollection/$',
        location_gis_collection.LocationGisCollectionList.as_view(),
        name='location_gis_collection'),
    re_path(r'^api/timbre/$', timbre.TimbreView.as_view(),
        name='timbre'),
    re_path(r'^api/timbre_ref/$', timbre_ref.TimbreRefView.as_view(),
        name='timbre_ref'),
    re_path(r'^globalsearch/$', global_search.GlobalSearchList.as_view(),
        name='search'),
    re_path(r'^versions/$', versions.VersionsView.as_view(), name='versions'),
]


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'block',
                block.BlockViewSet, basename='block')
router.register(r'institution',
                institution.InstitutionViewSet, basename='institution')
router.register(r'coupe', coupe.CoupeViewSet, basename='coupe')
router.register(r'cultural_area',
                cultural_area.CulturalAreaViewSet, basename='cultural_area')
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
router.register(r'civility', civility.CivilityViewSet, basename='civility'),
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
router.register(r'keyword',
                keyword.KeywordViewSet,
                basename='keyword')
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
router.register(r'ref_laforte',
                ref_laforte.RefLaforteViewSet,
                basename='ref_laforte')
router.register(r'skos_collection',
                skos_collection.SkosCollectionViewSet,
                basename='coirault')
router.register(r'skos_concept',
                skos_concept.SkosConceptViewSet,
                basename='coirault')


# Nested routers

# Authority's nested ------------------------------------
authority_router = routers.NestedSimpleRouter(
    router, r'authority', lookup='authority', trailing_slash=False)
authority_router.register(
    r'civilities', authority_civility.AuthorityCivilityViewSet)


# Fond's nested ------------------------------------
fond_router = routers.NestedSimpleRouter(
    router, r'fond', lookup='fond', trailing_slash=False)
fond_router.register(
    r'document', document_fond.DocumentFondViewSet)


# Mission's nested ------------------------------------
mission_router = routers.NestedSimpleRouter(
    router, r'mission', lookup='mission', trailing_slash=False)
mission_router.register(
    r'document', document_mission.DocumentMissionViewSet)


# Collection's nested ------------------------------------
collection_router = routers.NestedSimpleRouter(
    router, r'collection', lookup='collection', trailing_slash=False)
collection_router.register(
    r'collectors', collectioncollectors.CollectionCollectorsViewSet)
collection_router.register(
    r'cultural_areas', collection_cultural_area.CollectionCulturalAreaViewSet)
collection_router.register(
    r'informer', collection_informer.CollectionInformerViewSet)
collection_router.register(
    r'publisher', collection_publisher.CollectionPublisherViewSet)
collection_router.register(
    r'location', collection_location.CollectionLocationViewSet)
collection_router.register(
    r'language', collection_language.CollectionLanguageViewSet)
collection_router.register(
    r'performance', performance_collection.PerformanceCollectionViewSet)
performance_router = routers.NestedSimpleRouter(
    collection_router, r'performance', lookup='performance',
    trailing_slash=False)
performance_router.register(
    r'musician',
    performance_collection_musician.PerformanceCollectionMusicianViewSet)
collection_router.register(
    r'document', document_collection.DocumentCollectionViewSet)


# Item's nested ------------------------------------
item_router = routers.NestedSimpleRouter(
     router, r'item', lookup='item', trailing_slash=False)
item_router.register(
    r'collector', item_collector.ItemCollectorViewSet)
item_router.register(
    r'informer', item_informer.ItemInformerViewSet)
item_router.register(
    r'author', item_author.ItemAuthorViewSet)
item_router.register(
    r'compositor', item_compositor.ItemCompositorViewSet)
item_router.register(
    r'domain_song', item_domain_song.ItemDomainSongViewSet)
item_router.register(
    r'domain_music', item_domain_music.ItemDomainMusicViewSet)
item_router.register(
    r'domain_vocal', item_domain_vocal.ItemDomainVocalViewSet)
item_router.register(
    r'domain_tale', item_domain_tale.ItemDomainTaleViewSet)
item_router.register(
    r'usefulness', item_usefulness.ItemUsefulnessViewSet)
item_router.register(
    r'dance', item_dance.ItemDanceViewSet)
item_router.register(
    r'language', item_language.ItemLanguageViewSet)
item_router.register(
    r'keyword', item_keyword.ItemKeywordViewSet)
item_router.register(
    r'thematic', item_thematic.ItemThematicViewSet)
item_router.register(
    r'musical_organization',
    item_musical_organization.ItemMusicalOrganizationViewSet)
item_router.register(
    r'ref_laforte', item_ref_laforte.ItemRefLaforteViewSet)
item_router.register(
    r'coirault', item_coirault.ItemCoiraultViewSet
)
item_router.register(
    r'document', document_item.DocumentItemViewSet)
item_router.register(
    r'musical_group',
    item_musical_group.ItemMusicalGroupViewSet)
item_router.register(
    r'performance', item_performance.ItemPerformanceViewSet)
