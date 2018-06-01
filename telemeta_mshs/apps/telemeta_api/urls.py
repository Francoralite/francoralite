from rest_framework import routers
from .views import (
    authority,
    coupe,
    institution,
    MediaCollection)

router = routers.DefaultRouter()
router.register(r'institution',
                institution.InstitutionViewSet, base_name='institution')
router.register(r'coupe', coupe.CoupeViewSet, base_name='coupe')
router.register(r'authority',
                authority.AuthorityViewSet, base_name='authority')
router.register(r'collection',
                MediaCollection.MediacollectionViewSet,
                base_name='MediaCollection')
