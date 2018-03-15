#!/bin/bash

# stating apps
pip install -U django==1.8.18
pip uninstall -y south
# pip install django-environ redis
pip install -e git+https://github.com/Parisson/django-jqchat.git@dj1.8#egg=django-jqchat
pip install django-debug-toolbar==1.6
pip install -e git+https://github.com/Parisson/saved_searches.git@dj1.8#egg=saved_searches-2.0.0-beta

export PYTHONPATH=$PWD/telemeta_mshs/apps:$PYTHONPATH

# Starting celery worker with the --autoreload option will enable the worker to watch for file system changes
# This is an experimental feature intended for use in development only
# see http://celery.readthedocs.org/en/latest/userguide/workers.html#autoreloading
python ./manage.py celery worker --autoreload -A worker
