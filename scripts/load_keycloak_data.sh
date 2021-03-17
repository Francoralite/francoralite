#!/usr/bin/env bash

data_file_path=test_data/dump_keycloak.sql

if [ "$1" == "data" ]
then
    data_file_path="backups/dump_keycloak.sql"
fi

docker-compose stop keycloak \
    && docker-compose rm -f keycloak \
    && docker-compose stop keycloak_db \
    && docker-compose rm -f keycloak_db \
    && docker volume rm -f telemeta-integration_keycloak_db \
    && docker-compose up --no-start \
    && docker-compose start keycloak_db \
    && docker cp "${data_file_path}" telemeta-integration_keycloak_db_1:/tmp/keycloak_data.sql \
    && docker-compose exec keycloak_db bash -c "psql -U keycloak -W keycloak < '/tmp/keycloak_data.sql'" \
    && docker-compose up -d
