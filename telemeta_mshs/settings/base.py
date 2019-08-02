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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPuhTYR5350AMvQnCIZJSxjlD2NiSAEi05HTRMlK3/B1IjGwfg6lP+LXrhLHRXWg7L+EzIU9oiuPqzHr/pfdWor6fPiLpII6fkmBuB18SiM7cm3xe7fyfjwhN/q0Cu1ddSo1ILR0O6/bXWCV5DHdNAdtnSQRWdnRbJCSkjzJ9/KrArvcAUx1k1bCBQ8nJ60tNRZbmLrC+1rHe8+9m9b3NpI2IRkpfJynfuxcpDAQiJ3orW8Hy3g1dgueGsiS6FWnLF9zJc5JuZQVGFukpKcl7COPp2CSEwxgPxjyZQ4GBynCfuvoNHogTEbeujE/erRM3i5VD5C5miUXz/cYiaKmqwIDAQAB
-----END PUBLIC KEY-----"""
KEYCLOAK_CONFIG = {
    'KEYCLOAK_REALM':  'francoralite',
    'KEYCLOAK_CLIENT_ID': 'francoralite',
    'KEYCLOAK_DEFAULT_ACCESS': 'ALLOW',
    'KEYCLOAK_AUTHORIZATION_CONFIG': '/tmp/authorization_config.json',
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': 'DECODE',
    'KEYCLOAK_SERVER_URL': 'http://keycloak.francoralite.localhost:8080/auth/',
    'KEYCLOAK_CLIENT_SECRET_KEY': 'ade263c9-5aca-46d4-965f-6e2d188a2515',
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
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
)
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_RP_CLIENT_ID = 'francoralite'
OIDC_RP_CLIENT_SECRET = 'ade263c9-5aca-46d4-965f-6e2d188a2515'
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
