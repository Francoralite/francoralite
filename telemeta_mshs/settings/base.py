import environ
import os
import sys

# Original Telemeta application settings
# from .telemeta_settings import *  # noqa
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
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'telemeta_mshs.middleware.keycloak_mw.KeycloakMiddleware',
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
}

ROOT_URLCONF = 'telemeta_mshs.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'telemeta_mshs.wsgi.application'


#
# KEYCLOAK
#

# Excempt list - URL paths that doesn't need Keycloak Authorization
KEYCLOAK_BEARER_AUTHENTICATION_EXEMPT_PATHS = [
    'admin',
]
KEYCLOAK_RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz6eW9hkNixKdvpzabA0OGymXsPecAsq5EqBqw+8iJeb/cdUOhuF9y+1hR/ZDar11cC8LRGm1ERgCzXMeu0gBuRMWf3DOIRdMObVsZdWxKbQ3dZDgi7tpck8eGXKZCANhHqA0Xqm1q9E4Q4j5mAzzCs8hwk4uChCp6RpxKwOfNLqLg/IWr3NasoJ1mbLLTt/adHQdPprKHzqSkM+f5M1BY46RQ0pB4QnBb7UINk142AgHzmVD8mjLuUcK4HX4QDkRlswZw5yt1WoqWwuQuCR2/5KPE3XKC/FCI9dHuSUgWQN5rF2x2O7XNKlSicQ6ZmgNcSP7ZBFbfz3BtfTibgBauwIDAQAB
-----END PUBLIC KEY-----"""
KEYCLOAK_CONFIG = {
    'KEYCLOAK_REALM': os.getenv('KEYCLOAK_REALM', 'telemeta'),
    'KEYCLOAK_CLIENT_ID': os.getenv('KEYCLOAK_CLIENT_ID', 'telemeta'),
    'KEYCLOAK_DEFAULT_ACCESS': os.getenv('KEYCLOAK_DEFAULT_ACCESS', 'ALLOW'),
    'KEYCLOAK_AUTHORIZATION_CONFIG': os.getenv('KEYCLOAK_AUTHORIZATION_CONFIG', '/tmp/authorization_config.json'),
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': 'DECODE',
    'KEYCLOAK_SERVER_URL': os.getenv('KEYCLOAK_SERVER_URL', 'http://keycloak:8080/auth/'),
    'KEYCLOAK_CLIENT_SECRET_KEY': os.getenv('KEYCLOAK_CLIENT_SECRET_KEY', 'd67d8f45-a2b1-4059-85c3-33313487249c'),
    'KEYCLOAK_CLIENT_PUBLIC_KEY': KEYCLOAK_RSA_PUBLIC_KEY,
}


#
# CORS
#
CORS_ORIGIN_WHITELIST = (
    os.getenv('API_EXTERNAL_IP_ADDRESS', '1.2.3.4'),
    os.getenv('API_APP_EXTERNAL_URL', 'localhost'),
)
