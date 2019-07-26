import environ
import os
import sys

# Original Telemeta application settings
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
    'jsonrpc',
    'sorl.thumbnail',
    'timezones',
    'jqchat',
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

FRONT_HOST_URL = env('FRONT_HOST_URL')
USE_X_FORWARDED_HOST = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
}

ROOT_URLCONF = 'telemeta_mshs.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'telemeta_mshs.wsgi.application'


#
# CORS
#
CORS_ORIGIN_WHITELIST = (
    os.getenv('API_EXTERNAL_IP_ADDRESS', '1.2.3.4'),
    os.getenv('API_APP_EXTERNAL_URL', 'nginx.francoralite.localhost'),
)


#
# KEYCLOAK
#

# Default values
_KEYCLOAK_SERVER_URL = os.getenv(
    'KEYCLOAK_SERVER_URL', 'http://keycloak.francoralite.localhost:8080/auth/'
)
_KEYCLOAK_REALM = os.getenv('KEYCLOAK_REALM', 'francoralite')
_KEYCLOAK_CLIENT_ID =  os.getenv('KEYCLOAK_CLIENT_ID', 'francoralite'),
_KEYCLOAK_DEFAULT_ACCESS = os.getenv('KEYCLOAK_DEFAULT_ACCESS', 'ALLOW'),
_KEYCLOAK_CLIENT_SECRET_KEY = os.getenv(
    'KEYCLOAK_CLIENT_SECRET_KEY', 'ade263c9-5aca-46d4-965f-6e2d188a2515'
)
_KEYCLOAK_AUTHORIZATION_CONFIG = os.getenv(
    'KEYCLOAK_AUTHORIZATION_CONFIG', '/tmp/authorization_config.json'
)
_KEYCLOAK_METHOD_VALIDATE_TOKEN = os.getenv(
    'KEYCLOAK_METHOD_VALIDATE_TOKEN', 'DECODE'
)
_OPENID_BASE_URL = '{}{}{}{}'.format(
    _KEYCLOAK_SERVER_URL, 'realms/', _KEYCLOAK_REALM, '/protocol/openid-connect'
)

# Excempt list - URL paths that doesn't need Keycloak Authorization
KEYCLOAK_BEARER_AUTHENTICATION_EXEMPT_PATHS = [
    'admin',
]
_KEYCLOAK_RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPuhTYR5350AMvQnCIZJSxjlD2NiSAEi05HTRMlK3/B1IjGwfg6lP+LXrhLHRXWg7L+EzIU9oiuPqzHr/pfdWor6fPiLpII6fkmBuB18SiM7cm3xe7fyfjwhN/q0Cu1ddSo1ILR0O6/bXWCV5DHdNAdtnSQRWdnRbJCSkjzJ9/KrArvcAUx1k1bCBQ8nJ60tNRZbmLrC+1rHe8+9m9b3NpI2IRkpfJynfuxcpDAQiJ3orW8Hy3g1dgueGsiS6FWnLF9zJc5JuZQVGFukpKcl7COPp2CSEwxgPxjyZQ4GBynCfuvoNHogTEbeujE/erRM3i5VD5C5miUXz/cYiaKmqwIDAQAB
-----END PUBLIC KEY-----"""
KEYCLOAK_CONFIG = {
    'KEYCLOAK_REALM': _KEYCLOAK_REALM,
    'KEYCLOAK_CLIENT_ID': _KEYCLOAK_CLIENT_ID,
    'KEYCLOAK_DEFAULT_ACCESS': _KEYCLOAK_DEFAULT_ACCESS,
    'KEYCLOAK_AUTHORIZATION_CONFIG': _KEYCLOAK_AUTHORIZATION_CONFIG,
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': _KEYCLOAK_METHOD_VALIDATE_TOKEN,
    'KEYCLOAK_SERVER_URL': _KEYCLOAK_SERVER_URL,
    'KEYCLOAK_CLIENT_SECRET_KEY': _KEYCLOAK_CLIENT_SECRET_KEY,
    'KEYCLOAK_CLIENT_PUBLIC_KEY': _KEYCLOAK_RSA_PUBLIC_KEY,
}

AUTHENTICATION_BACKENDS = (
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
)
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_RP_CLIENT_ID = _KEYCLOAK_CLIENT_ID
OIDC_RP_CLIENT_SECRET = _KEYCLOAK_CLIENT_SECRET_KEY
OIDC_CREATE_USER = True

OIDC_OP_AUTHORIZATION_ENDPOINT = _OPENID_BASE_URL + '/auth'
OIDC_OP_TOKEN_ENDPOINT = _OPENID_BASE_URL + '/token'
OIDC_OP_USER_ENDPOINT  = _OPENID_BASE_URL + '/userinfo'
OIDC_OP_JWKS_ENDPOINT  = _OPENID_BASE_URL + '/certs'

LOGIN_REDIRECT_URL = os.getenv(
    'LOGIN_REDIRECT_URL', 'http://nginx.francoralite.localhost:8080/'
)
LOGOUT_REDIRECT_URL = _OPENID_BASE_URL + '/logout'
