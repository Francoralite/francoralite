from rest_framework import routers
from .views import authority
from .views import coupe
from .views import institution

router = routers.DefaultRouter()
router.register(r'institution',
                institution.InstitutionViewSet, base_name='institution')
router.register(r'coupe', coupe.CoupeViewSet, base_name='coupe')
router.register(r'authority',
                authority.AuthorityViewSet, base_name='authority')
