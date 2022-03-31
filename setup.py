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
  name = "Francoralite",
  url = "http://francoralite.org",
  description = "Open web audio application with semantics",
  long_description = open('README.md').read(),
  author = "Luc Leger",
  author_email = "leger.luc@gmail.com",
  version = '1.7.0',
  install_requires = [
    'django==3.1.14',
    'django-appconf==1.0.4',
    'django-environ==0.4.5',
    'django-filter==2.4.0',
    'djangorestframework==3.12.2',
    'djangorestframework-xml==2.0.0',
    'drf-nested-routers==0.93.3',
    'drf-yasg==1.20.0',
    'gunicorn==20.0.4',
    # V2
    'django-model-utils==4.1.1',
    'psycopg2-binary==2.8.6',
    'pyaml==20.4.0',
    'django-google-tools==1.1.0', # Always useful ?
    #'MySQL-python==1.2.5',
    'mysqlclient==2.0.3',
    # V3
    'django-registration-redux==2.9',
    'django-extensions==3.1.1',
    'django-timezones', # Always useful ?
    'django-debug-toolbar==3.2.1',
    'django-extra-views==0.13.0',
    'django-breadcrumbs==1.1.3', # Always useful ?
    'django-bootstrap3==14.2.0',
    'django-bootstrap-datepicker==1.4.0',
    'django-bower==5.2.0',
    'pyyaml==5.4.1',
    'Werkzeug==1.0.1',
    'django-dirtyfields==1.5.0',
    'sqlparse==0.4.2',
    'django-markdownx==3.0.1',
    'django_select2==7.6.2',
    'lxml==4.6.5',
    'django-leaflet==0.28.1',
    'django-geojson==3.1.0',
    'django-cors-headers==3.7.0',
    'python-keycloak==0.26.1',
    'rsa==4.7.2',
    'python-jose==3.3.0',
    'mozilla-django-oidc==2.0.0',
    'rdflib==5.0.0',
  ],
  extras_require={
    'tests': [
      'factory_boy==3.2.0',
      'ipython==7.21.0',
      'parameterized==0.8.1',
      'pytest==6.2.2',
      'pytest-cov==2.11.1',
      'pytest-django==4.1.0',
      'pytest-env==0.6.2',
      'pytest-pythonpath==0.7.3',
      'coveralls==3.0.1',
      'selenium==4.1.0',
      'coverage==5.5',
      'coveragepy-lcov==0.1.1',
      'icecream==2.1.1',
    ],
  },
  platforms = ['OS Independent'],
  license = 'CeCILL v2',
  classifiers = CLASSIFIERS,
  packages = find_packages(),
  include_package_data = True,
  zip_safe = False,
)
