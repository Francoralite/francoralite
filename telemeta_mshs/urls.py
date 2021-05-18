import os

from django.conf import settings
from django.conf.urls import url, include
#from django.contrib import admin
from django.http import HttpResponse
#from django.views.i18n import javascript_catalog

from rest_framework import permissions
from rest_framework.schemas import get_schema_view

# OpenAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Apps urls
from .apps.telemeta_api import urls as telemeta_api_urls
from .apps.telemeta_front import urls as telemeta_front_urls

# AuthenticationFailed
import mozilla_django_oidc.urls

# OpenAPI management
schema_view = get_schema_view(
   openapi.Info(
      title="Francoralite API",
      default_version='v1',
      description="Francoralite API",
      terms_of_service="https://francoralite.net/legal/", # FIXME: A valider !
      contact=openapi.Contact(email="contact@francoralite.net"),
      license=openapi.License(name="MIT License"), # FIXME: A valider !
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# admin.autodiscover()

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
robots_rules = open(PROJECT_ROOT + os.sep + 'robots.txt', 'r').read()

urlpatterns = [
    # New frontend endpoints
    url(r'', include(telemeta_front_urls)),

#    url(r'^admin/django/', include(admin.site.urls)),
    url(r'^', include(telemeta_api_urls)),
    url(r'^api/', include(telemeta_api_urls.router.urls)),
    url(r'^api/', include(telemeta_api_urls.Fond_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Mission_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Collection_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Performance_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Item_router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^oidc/', include(mozilla_django_oidc.urls)),

    # Languages
#    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^robots\.txt$', lambda r: HttpResponse(
        robots_rules, content_type="text/plain")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
