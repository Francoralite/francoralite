#!/bin/bash

export PYTHONPATH=$PWD/telemeta_mshs/apps:$PYTHONPATH

# Starting celery worker with the --autoreload option will enable the worker to watch for file system changes
# This is an experimental feature intended for use in development only
# see http://celery.readthedocs.org/en/latest/userguide/workers.html#autoreloading
python ./manage.py celery worker --autoreload -A worker
