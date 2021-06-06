import os

# Reminder
ALLOWED_HOSTS = ['*']
PROJECT_ROOT = '/srv/app/'
TIME_ZONE = 'Europe/Paris'
LANGUAGES = [('fr', 'French'),
             ('en', 'English'),
             ('de', 'German'),
             ('es', 'Spanish'),
             ]
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = '/srv/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/srv/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = os.getenv('SECRET_KEY')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
AUTH_USER_MODEL = 'auth.User'

# Settings for django-bootstrap3
BOOTSTRAP3 = {
    'set_required': True,
    'set_placeholder': False,
    'error_css_class': 'has-error',
    'required_css_class': 'has-warning',
    'javascript_in_head': True,
}

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('APP_LOG_LEVEL'),
    },
}


INSTALLED_APPS = (
    'django.contrib.auth',
    'mozilla_django_oidc',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
#    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django_extensions',
    'timezones',
    'bootstrap3',
    'bootstrap_datepicker',
    'bootstrap_pagination',
    'registration',
    'rest_framework',
    'rest_framework_xml',
    'django',
    'drf_yasg',
    'django_filters',
    'francoralite.apps.francoralite_api',
    'francoralite.apps.francoralite_front',
    'django_select2',
    'leaflet',
    'markdownx',
    'corsheaders',
    'rdflib',
    # Check if always needed
    'extra_views',
)

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'francoralite.middleware.keycloak_mw.KeycloakMiddleware',
    'francoralite.middleware.session_history.SessionHistoryMiddleware',
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
            'NAME': 'francoralite_testing',
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

ROOT_URLCONF = 'francoralite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'francoralite.wsgi.application'


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
    'KEYCLOAK_REALM': os.getenv('KEYCLOAK_REALM'),
    'KEYCLOAK_CLIENT_ID': os.getenv('KEYCLOAK_CLIENT_ID'),
    'KEYCLOAK_DEFAULT_ACCESS': os.getenv('KEYCLOAK_DEFAULT_ACCESS'),
    'KEYCLOAK_AUTHORIZATION_CONFIG': os.getenv('KEYCLOAK_AUTHORIZATION_CONFIG'),
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': os.getenv('KEYCLOAK_METHOD_VALIDATE_TOKEN'),
    'KEYCLOAK_SERVER_URL': os.getenv('KEYCLOAK_SERVER_URL'),
    'KEYCLOAK_CLIENT_SECRET_KEY': os.getenv('KEYCLOAK_CLIENT_SECRET_KEY'),
    'KEYCLOAK_CLIENT_PUBLIC_KEY': KEYCLOAK_RSA_PUBLIC_KEY,
}


#
# CORS
#
CORS_ORIGIN_WHITELIST = (
    'http://1.2.3.4',
    'http://nginx.francoralite.localhost',
)

AUTHENTICATION_BACKENDS = (
    'francoralite_api.oidc.myoidcab.MyOIDCAB',
)

_OIDC_BASE_URL = "{}realms/{}/protocol/openid-connect".format(os.getenv('KEYCLOAK_SERVER_URL'), os.getenv('KEYCLOAK_REALM'))
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_RP_CLIENT_ID = os.getenv('KEYCLOAK_CLIENT_ID')
OIDC_RP_CLIENT_SECRET = os.getenv('KEYCLOAK_CLIENT_SECRET_KEY')
OIDC_CREATE_USER = True
OIDC_STORE_ACCESS_TOKEN = True
OIDC_STORE_ID_TOKEN = True

OIDC_OP_AUTHORIZATION_ENDPOINT = "{}/auth".format(_OIDC_BASE_URL)
OIDC_OP_TOKEN_ENDPOINT = "{}/token".format(_OIDC_BASE_URL)
OIDC_OP_USER_ENDPOINT = "{}/userinfo".format(_OIDC_BASE_URL)
OIDC_OP_JWKS_ENDPOINT = "{}/certs".format(_OIDC_BASE_URL)

LOGIN_REDIRECT_URL = os.getenv('APP_BASE_URL')
LOGOUT_REDIRECT_URL = "{}/logout".format(_OIDC_BASE_URL)


#
# DEBUG MANAGEMENT
#
if os.getenv('DEBUG').lower() == "true":
    DEBUG = True
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
    }
    INTERNAL_IPS = ['127.0.0.1', '0.0.0.0', '172.17.0.1']
