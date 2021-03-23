#!/bin/bash

export PYTHONPATH=$PWD/telemeta_mshs/apps:$PYTHONPATH

python ./manage.py migrate --noinput -v 3
python ./manage.py bower_install -- --allow-root

if [ "${REINDEX}" = "True" ]; then
    python ./manage.py rebuild_index --noinput
fi

python ./manage.py collectstatic --noinput

# Fix media access rights
find /srv/media -exec chown www-data:www-data {} \;
find /srv/static -exec chown www-data:www-data {} \;

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn telemeta_mshs.wsgi:application \
        --bind :8000 \
        --workers 3
