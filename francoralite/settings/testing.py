from .base import *  # noqa

MEDIA_ROOT = '/srv/media/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
#    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django_extensions',
    'leaflet',
    'rest_framework',
    'drf_yasg',
    'francoralite.apps.francoralite_api',
    'francoralite.apps.francoralite_front',
    'rdflib',
    'selenium',
    'bootstrap3',
)

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
FRONT_HOST_URL = 'http://localhost:8000'
_OIDC_BASE_URL = "{}realms/{}/protocol/openid-connect".format(os.getenv('KEYCLOAK_SERVER_URL'), os.getenv('KEYCLOAK_REALM'))
LOGOUT_REDIRECT_URL = "{}/logout?redirect_uri={}".format(_OIDC_BASE_URL, FRONT_HOST_URL)
