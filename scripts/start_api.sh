#!/bin/bash

export PYTHONPATH=$PWD/telemeta_mshs/apps:$PYTHONPATH

django-admin migrate --noinput -v 3
django-admin bower_install --allow-root

if [ "${REINDEX}" = "True" ]; then
    django-admin rebuild_index --noinput
fi

django-admin collectstatic --noinput

# Fix media access rights
find /srv/bower -exec chown www-data:www-data {} \;
find /srv/media -exec chown www-data:www-data {} \;
find /srv/static -exec chown www-data:www-data {} \;

if [ "${LOCAL_DEV}" = "True" ]; then
    # Start Django internal server
    echo Starting Django web server.
    exec django-admin runserver 0.0.0.0:8000
else
    # Start Gunicorn processes
    echo Starting Gunicorn.
    exec gunicorn telemeta_mshs.wsgi:application \
            --bind :8000 \
            --workers 3
fi
