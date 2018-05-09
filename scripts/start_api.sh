#!/bin/bash

# paths
app='/srv/app'
static='/srv/static/'
wsgi='/srv/app/telemeta_mshs/wsgi.py'
media='/srv/media/'
src='/srv/src/'
log='/var/log/uwsgi/app.log'

# uwsgi params
port=8000
processes=8
threads=8
autoreload=3
uid='www-data'
gid='www-data'

export PYTHONPATH=$PWD/telemeta_mshs/apps:$PYTHONPATH

python ./manage.py syncdb
python ./manage.py migrate --noinput -v 3
python ./manage.py bower_install -- --allow-root

# telemeta setup
python ./manage.py telemeta-create-admin-user
python ./manage.py telemeta-create-boilerplate
python ./manage.py telemeta-setup-enumerations

# Delete Timeside database if it exists
cat ./telemeta_mshs/apps/Telemeta/scripts/sql/drop_timeside.sql | python ./manage.py dbshell

if [ $REINDEX = "True" ]; then
    python ./manage.py rebuild_index --noinput
fi

# choose dev or prod mode
if [ "$1" = "--runserver" ]; then
    python ./manage.py runserver 0.0.0.0:8000
else
    python ./manage.py collectstatic --noinput

    # fix media access rights
    find $media -maxdepth 1 -path ${media}import -prune -o -type d -not -user www-data -exec chown www-data:www-data {} \;

    # Start UWSGI processes
    uwsgi --socket :$port --wsgi-file $wsgi --chdir $app --master \
    --processes $processes --threads $threads \
    --uid $uid --gid $gid --logto $log --touch-reload $wsgi
fi
