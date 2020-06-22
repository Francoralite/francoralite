import os


# Original Telemeta application settings
# from .telemeta_settings import *  # noqa
from telemeta_settings import *  # noqa

INSTALLED_APPS = (
    'django.contrib.auth',
    'mozilla_django_oidc',  # Load after auth
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
    'rest_framework_xml',
    'djcelery',
    'haystack',
    'djangobower',
    'django',
    'saved_searches',
    'rest_framework_swagger',
    'django_filters',
    'telemeta_mshs.apps.telemeta_api',
    'telemeta_mshs.apps.telemeta_front',
    'django_select2',
    'leaflet',
    'markdownx',
    'corsheaders',
    'debug_toolbar',
    'rdflib',
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
    'telemeta_mshs.middleware.session_history.SessionHistoryMiddleware',
    # 'telemeta_mshs.middleware.history_records.HistoryRecordsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'NAME': os.getenv('MYSQL_DATABASE'),
        'HOST': 'db',
        'PORT': '3306',
        'TEST': {
            'NAME': 'telemeta_testing',
            'USER': 'root'
        }
    }
}

APPEND_SLASH = False

FRONT_HOST_URL = 'http://localhost:8000'
FRONT_HOST_URL_EXTERNAL = 'http://nginx.francoralite.localhost:8080'
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
USE_X_FORWARDED_PROTO = True

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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgP/m+V2owmzi6egBGQekKThsXuSDsEKfWjYNk9quCCR4BBFlT0444b1xb948w7Ii59OFor3UDfvy8+mD9XSm56ghuWhvuvAcOEGYPlvqOPQ+p5IXum1b7LrjH1aljtDmT6C6No1D+POzsLy9MQBRto7zTbi3ViQoh+7tMywUPm6WreYxpwPTDhSCA2+uptPJn2R5vqi/OB4wIvQ90JXvH6RE5oSkmHSMW10UWRFGNtCABJy4XXlCXDDl6BW+uTuy1LvVZxDiqBudqEmsbeVl2gXGp46BRqs+YDabh10V7rkuF4XeHY4bU3ICfWu+1Zq7fRF1Em/cMVuUfjKXy3dKZwIDAQAB
-----END PUBLIC KEY-----"""
KEYCLOAK_CONFIG = {
    'KEYCLOAK_REALM':  'francoralite',
    'KEYCLOAK_CLIENT_ID': 'francoralite',
    'KEYCLOAK_DEFAULT_ACCESS': 'ALLOW',
    'KEYCLOAK_AUTHORIZATION_CONFIG': '/tmp/authorization_config.json',
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': 'DECODE',
    'KEYCLOAK_SERVER_URL': 'http://keycloak.francoralite.localhost:8080/auth/',
    'KEYCLOAK_CLIENT_SECRET_KEY': 'cc453f2d-9342-4924-bbb9-53f3eda5e824',
    'KEYCLOAK_CLIENT_PUBLIC_KEY': KEYCLOAK_RSA_PUBLIC_KEY,
}


#
# CORS
#
CORS_ORIGIN_WHITELIST = (
    '1.2.3.4',
    'nginx.francoralite.localhost',
)

AUTHENTICATION_BACKENDS = (
    'telemeta_api.oidc.myoidcab.MyOIDCAB',
)
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_RP_CLIENT_ID = 'francoralite'
OIDC_RP_CLIENT_SECRET = 'cc453f2d-9342-4924-bbb9-53f3eda5e824'
OIDC_CREATE_USER = True

OIDC_OP_AUTHORIZATION_ENDPOINT = \
    'http://keycloak.francoralite.localhost:8080/auth/' +\
    "realms/francoralite/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = 'http://keycloak.francoralite.localhost:8080/auth/' +\
    "realms/francoralite/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = 'http://keycloak.francoralite.localhost:8080/auth/' +\
    "realms/francoralite/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = 'http://keycloak.francoralite.localhost:8080/auth/' +\
    "realms/francoralite/protocol/openid-connect/certs"


LOGIN_REDIRECT_URL = "http://nginx.francoralite.localhost:8080/"
LOGOUT_REDIRECT_URL = 'http://keycloak.francoralite.localhost:8080/auth/' +\
    "realms/francoralite/protocol/openid-connect/logout"

#
# BOWER
#
BOWER_PATH = '/usr/bin/bower'
