import environ
import os
import sys

# Original Telemeta application settings
from telemeta_settings import *  # noqa


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'suit',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django_extensions',
    'telemeta',
    'timeside.player',
    # 'timeside.server',
    'jsonrpc',
    'sorl.thumbnail',
    'timezones',
    'jqchat',
    # 'ipauth',
    'extra_views',
    'bootstrap3',
    'bootstrap_datepicker',
    'bootstrap_pagination',
    'registration',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'djcelery',
    'haystack',
    'djangobower',
    'djng',
    'saved_searches',
    'rest_framework_swagger',
    'django_filters',
    'telemeta_mshs.apps.telemeta_api',
    'telemeta_mshs.apps.telemeta_front',
    'django_select2',
    'leaflet',
    'markdownx',
)

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASSWORD'),
        'NAME': env('MYSQL_DATABASE'),
        'HOST': 'db',
        'PORT': '3306',
        'TEST': {
            'NAME': 'telemeta_testing',
            'USER': 'root'
        }
    }
}

FRONT_HOST_URL = 'http://localhost:8000'
USE_X_FORWARDED_HOST = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

}

ROOT_URLCONF = 'telemeta_mshs.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'telemeta_mshs.wsgi.application'
