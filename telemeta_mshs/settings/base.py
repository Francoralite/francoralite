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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsAfGsWzaAXvYLu7FcRKwqxqdF3K/On7qcClgP+4CEPUfeEGFEc9PGfy75XWHzVOidO0AG0fmkNG5j2GDcvDp/QCDCmRv6fY6O5Oz3gaG9TTMp93n/Jyd1cF+LubmCYpT77jMl/Ulkw3ndh+KFzLXhYmH+tN6cQcxvT5ovlq2eqtxWRcA8PETkZwlECPdjNnQ9yC8zezokkbB0I6p1rssg/9hQ6aIvGZYFdFOINrbQUqszRxiL2jj5ujZQZgLbAh93XBC9ucpWRGtvl9oSICUj2dtXpTCdCGh4/pDMnik+MDSAL3vN91/tQ2EBmwGqlnNwjJLy2w8PK5iMUMfuONN0wIDAQAB
-----END PUBLIC KEY-----"""
KEYCLOAK_CONFIG = {
    'KEYCLOAK_REALM': os.getenv('KEYCLOAK_REALM', 'francoralite'),
    'KEYCLOAK_CLIENT_ID': os.getenv('KEYCLOAK_CLIENT_ID', 'francoralite'),
    'KEYCLOAK_DEFAULT_ACCESS': os.getenv('KEYCLOAK_DEFAULT_ACCESS', 'ALLOW'),
    'KEYCLOAK_AUTHORIZATION_CONFIG': os.getenv('KEYCLOAK_AUTHORIZATION_CONFIG', '/tmp/authorization_config.json'),
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': 'DECODE',
    'KEYCLOAK_SERVER_URL': os.getenv('KEYCLOAK_SERVER_URL', 'http://keycloak:8080/auth/'),
    'KEYCLOAK_CLIENT_SECRET_KEY': os.getenv('KEYCLOAK_CLIENT_SECRET_KEY', 'b2412c7c-b1f9-4f31-a799-55aa98f55dcf'),
    'KEYCLOAK_CLIENT_PUBLIC_KEY': KEYCLOAK_RSA_PUBLIC_KEY,
}


#
# CORS
#
CORS_ORIGIN_WHITELIST = (
    os.getenv('API_EXTERNAL_IP_ADDRESS', '1.2.3.4'),
    os.getenv('API_APP_EXTERNAL_URL', 'localhost'),
)
