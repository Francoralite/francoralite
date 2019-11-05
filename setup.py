# -*- coding: utf-8 -*-

import multiprocessing
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import sys


CLASSIFIERS = ['Environment :: Web Environment',
'Framework :: Django',
'Intended Audience :: Science/Research',
'Intended Audience :: Education',
'Programming Language :: Python',
'Programming Language :: JavaScript',
'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
'Topic :: Multimedia :: Sound/Audio',
'Topic :: Multimedia :: Sound/Audio :: Analysis',
'Topic :: Multimedia :: Sound/Audio :: Players',
'Topic :: Scientific/Engineering :: Information Analysis',
'Topic :: System :: Archiving',  ]


setup(
  name = "Telemeta-MSHS",
  url = "http://telemeta-mshs.org",
  description = "Open web audio application with semantics",
  long_description = open('README.md').read(),
  author = "Luc Leger",
  author_email = "leger.luc@gmail.com",
  version = '1.7.0',
  install_requires = [
    'django==1.8.18',
    'django-environ==0.4.4',
    'django-haystack==2.5.1',
    'django-ipauth @ git+https://github.com/yomguy/django-ipauth.git#egg=django-ipauth-0.4.1-dev', # noqa
    'django-jqchat',
    'django-rest-swagger==2.2.0',
    'djangorestframework==3.6.4',
    'djangorestframework-xml==1.4.0',
    'drf-nested-routers==0.90.0',
    'django-filter==1.0.0',
    'ebooklib==0.16',
    'gunicorn==19.7.1',
    'saved_searches @ git+https://github.com/Parisson/saved_searches.git@dj1.8#egg=saved_searches-2.0.0-beta', # noqa
    'sorl-thumbnail-master-0 @ git+https://github.com/mariocesar/sorl-thumbnail.git@7ce76bc1ef798a63cbf89b5df83de4da4b12e98d#egg=sorl-thumbnail-master-0',  # noqa
    'telemeta @ git+https://github.com/Parisson/Telemeta.git@9c6a77974b338781db2971d66c96834b94ab2bb8#egg=telemeta-1.7.0-dev',  # noqa
    # 'timeside==0.7', # See https://github.com/Parisson/TimeSide/issues/104
    'timeside-master @ git+https://github.com/Parisson/TimeSide.git@86f699cd61db2c0dc7fed61c4bb9f44ca3d8868f#egg=timeside-master-0', # noqa
    # V2
    'django-model-utils==3.1.1',
    'psycopg2-binary==2.7.4',
    'pyaml==17.12.1',
    'django-google-tools==1.1.0',
    'MySQL-python==1.2.5',
    # V3
    'django-registration-redux',
    'django-extensions',
    'django-timezones',
    'django-debug-toolbar==1.6',
    'django-extra-views',
    'django-breadcrumbs',
    'django-bootstrap3==8.1.0',
    'django-bootstrap-datepicker==1.1.1',
    'django-bootstrap-pagination',
    'django-json-rpc',
    'django-suit',
    'django-celery',
    'docutils',
    'psutil',
    'pyyaml',
    'python-ebml',
    'zipstream',
    'elasticsearch==1.6.0',
    'redis',
    'Werkzeug',
    'django-dirtyfields==1.2.1',
    'sqlparse==0.2.2',
    'django-markdownx',
    'django_select2==5.11.1',
    'lxml',
    'django-leaflet==0.24.0',
    'django-geojson==2.11.0',
    'django-cors-headers==2.4.1',
    'python-keycloak==0.16.0',
    'python-jose==3.0.1',
    'mozilla-django-oidc @ git+https://github.com/lluc/mozilla-django-oidc.git@francoralite#egg=mozilla-django-oidc-francoralite', # noqa
  ],
  extras_require={
    'tests': [
      'factory_boy==2.10.0',
      'ipython==5.5.0',
      'parameterized==0.6.1',
      'pytest==3.4.2',
      'pytest-cov==2.5.1',
      'pytest-django==3.1.2',
      'pytest-env==0.6.2',
      'pytest-pythonpath==0.7.2',
    ],
  },
  platforms = ['OS Independent'],
  license = 'CeCILL v2',
  classifiers = CLASSIFIERS,
  packages = find_packages(),
  include_package_data = True,
  zip_safe = False,
)
