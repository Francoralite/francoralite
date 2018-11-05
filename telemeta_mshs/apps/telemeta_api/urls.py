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
    media_item,
    ext_media_item,
    )

router = routers.SimpleRouter()
router.register(r'institution',
                institution.InstitutionViewSet, base_name='institution')
router.register(r'coupe', coupe.CoupeViewSet, base_name='coupe')
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
router.register(r'item',
                media_item.MediaItemViewSet,
                base_name='MediaItem')
router.register(r'extitem',
                ext_media_item.ExtMediaItemViewSet,
                base_name='ExtMediaItem')


# Nested routers
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

router.register(
    r'extitems', ext_media_item.ExtMediaItemViewSet)
