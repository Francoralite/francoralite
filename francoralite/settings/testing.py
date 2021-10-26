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
