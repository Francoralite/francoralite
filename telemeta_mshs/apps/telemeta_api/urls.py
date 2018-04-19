from django.conf.urls import url, include
from rest_framework import routers
from .views import authority
from .views import institution

router = routers.DefaultRouter()
router.register(r'institution', institution.InstitutionViewSet, base_name='institution')
router.register(r'authority', authority.AuthorityViewSet, base_name='authority')
