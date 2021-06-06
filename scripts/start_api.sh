#!/bin/bash

export PYTHONPATH=$PWD/francoralite/apps:$PYTHONPATH

django-admin migrate --noinput -v 3

if [ "${REINDEX}" = "True" ]; then
    django-admin rebuild_index --noinput
fi

django-admin collectstatic --noinput

# Fix media access rights
find /srv/media -exec chown www-data:www-data {} \;
find /srv/static -exec chown www-data:www-data {} \;

if [ "${LOCAL_DEV}" = "True" ]; then
    # Start Django internal server
    echo Starting Django web server.
    exec django-admin runserver 0.0.0.0:8000
else
    # Start Gunicorn processes
    echo Starting Gunicorn.
    exec gunicorn francoralite.wsgi:application \
            --bind :8000 \
            --workers 3
fi
