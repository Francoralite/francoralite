import environ
import os
import sys

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

FRONT_HOST_URL = 'http://app-francoralite-test.huma-num.fr:8000'
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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhHDfEYJu9eS9ZQPgbwz8dVVpdHp1aaco0yOvKTVpjWfCWQpXqqDASrh4j7ycbiR0Vbgsvz3UPOXh4KgglpTLjN++3wIQ1xfiBfqxBdfj7otZy8JmbfhI5VyxUK4Gr7xrZcZ0qC64GS6ZgiXx1iHiupp/Ivn9ac7jO0jAkwqV9pxOsTqMFWQJ41IQnFRDWyIVLjgKLz5ybaoiJ4p9W3RUiDHigd6hW6ne+VlDLt0GjxilCcrL4JngszYYygnalJKUsgXM28NHNj8hco1FCHfQtHemKc+ck8fYlNkdS/sqNUNF+pBjfIRsCCX4hjwtvVH0T5gNDjt6Ar+junXMFLu5ywIDAQAB
-----END PUBLIC KEY-----"""
KEYCLOAK_CONFIG = {
    'KEYCLOAK_REALM': os.getenv('KEYCLOAK_REALM', 'francoralite'),
    'KEYCLOAK_CLIENT_ID': os.getenv('KEYCLOAK_CLIENT_ID', 'francoralite'),
    'KEYCLOAK_DEFAULT_ACCESS': os.getenv('KEYCLOAK_DEFAULT_ACCESS', 'ALLOW'),
    'KEYCLOAK_AUTHORIZATION_CONFIG': os.getenv(
        'KEYCLOAK_AUTHORIZATION_CONFIG', '/tmp/authorization_config.json'),
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': 'DECODE',
    'KEYCLOAK_SERVER_URL': os.getenv(
        'KEYCLOAK_SERVER_URL', 'http://auth-francoralite-test.huma-num.fr:8080/auth/'),
    'KEYCLOAK_CLIENT_SECRET_KEY': os.getenv(
        'KEYCLOAK_CLIENT_SECRET_KEY', '76c8ea71-a26d-4ba8-a5f9-1411dfdf684b'),
    'KEYCLOAK_CLIENT_PUBLIC_KEY': KEYCLOAK_RSA_PUBLIC_KEY,
}


#
# CORS
#
CORS_ORIGIN_WHITELIST = (
    os.getenv('API_EXTERNAL_IP_ADDRESS', '1.2.3.4'),
    os.getenv('API_APP_EXTERNAL_URL', 'app-francoralite-test.huma-num.fr'),
)

AUTHENTICATION_BACKENDS = (
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
)
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_RP_CLIENT_ID = os.getenv('KEYCLOAK_CLIENT_ID', 'francoralite')
OIDC_RP_CLIENT_SECRET = os.getenv(
    'KEYCLOAK_CLIENT_SECRET_KEY', '76c8ea71-a26d-4ba8-a5f9-1411dfdf684b')
OIDC_CREATE_USER = True

OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv(
    'KEYCLOAK_SERVER_URL', 'https://auth-francoralite-test.huma-num.fr/auth/') +\
    "realms/francoralite/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = os.getenv(
    'KEYCLOAK_SERVER_URL', 'https://auth-francoralite-test.huma-num.fr/auth/') +\
    "realms/francoralite/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = os.getenv(
    'KEYCLOAK_SERVER_URL', 'https://auth-francoralite-test.huma-num.fr/auth/') +\
    "realms/francoralite/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = os.getenv(
    'KEYCLOAK_SERVER_URL', 'https://auth-francoralite-test.huma-num.fr/auth/') +\
    "realms/francoralite/protocol/openid-connect/certs"

LOGIN_REDIRECT_URL = "https://app-francoralite-test.huma-num.fr/"
OIDC_REDIRECT_REQUIRE_HTTPS = True
LOGOUT_REDIRECT_URL = os.getenv(
    'KEYCLOAK_SERVER_URL', 'https://auth-francoralite-test.huma-numfr/auth/') +\
    "realms/francoralite/protocol/openid-connect/logout"
