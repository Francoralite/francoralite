import os

from django.contrib import admin
from django.conf.urls import url, include
from django.http import HttpResponse
from django.views.i18n import javascript_catalog

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# Apps urls
from .apps.telemeta_api import urls as telemeta_api_urls
from .apps.telemeta_front import urls as telemeta_front_urls

# AuthenticationFailed
import mozilla_django_oidc.urls

# Create our schema's view w/ the get_schema_view() helper method.
#   Pass in the proper Renderers for swagger
schema_view = get_schema_view(
    title='Users API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

admin.autodiscover()

js_info_dict = {
    'packages': ('telemeta',),
}

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
robots_rules = open(PROJECT_ROOT + os.sep + 'robots.txt', 'r').read()

urlpatterns = [
    # New frontend endpoints
    url(r'', include(telemeta_front_urls)),

    # Telemeta orignal app
    url(r'', include('telemeta.urls')),

    url(r'^admin/django/', include(admin.site.urls)),
    url(r'^', include(telemeta_api_urls)),
    url(r'^api/', include(telemeta_api_urls.router.urls)),
    url(r'^api/', include(telemeta_api_urls.Fond_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Mission_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Collection_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Performance_router.urls)),
    url(r'^api/', include(telemeta_api_urls.Item_router.urls)),
    url(r'^docs/', schema_view, name="docs"),
    url(r'^oidc/', include(mozilla_django_oidc.urls)),

    # Languages
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    url(r'^robots\.txt$', lambda r: HttpResponse(
        robots_rules, content_type="text/plain")),
]
