import os

from django.conf import settings
from django.conf.urls import re_path, include
#from django.contrib import admin
from django.http import HttpResponse
#from django.views.i18n import javascript_catalog

from rest_framework import permissions
from rest_framework.schemas import get_schema_view

# OpenAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Apps urls
from .apps.francoralite_api import urls as francoralite_api_urls
from .apps.francoralite_front import urls as francoralite_front_urls
from .apps.francoralite_front.views.errors import (
    handler403, handler404, handler500)

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
    re_path(r'', include(francoralite_front_urls)),

#    re_path(r'^admin/django/', include(admin.site.urls)),
    re_path(r'^', include(francoralite_api_urls)),
    re_path(r'^api/', include(francoralite_api_urls.router.urls)),
    re_path(r'^api/', include(francoralite_api_urls.fond_router.urls)),
    re_path(r'^api/', include(francoralite_api_urls.mission_router.urls)),
    re_path(r'^api/', include(francoralite_api_urls.collection_router.urls)),
    re_path(r'^api/', include(francoralite_api_urls.performance_router.urls)),
    re_path(r'^api/', include(francoralite_api_urls.item_router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^oidc/', include(mozilla_django_oidc.urls)),

    # Languages
#    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^robots\.txt$', lambda r: HttpResponse(
        robots_rules, content_type="text/plain")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
