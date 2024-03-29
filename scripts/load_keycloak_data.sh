#!/usr/bin/env bash

data_file_path=test_data/dump_keycloak.sql
current_folder=$(basename $PWD)

if [ "$1" == "data" ]
then
    data_file_path="backups/dump_keycloak.sql"
fi

docker-compose stop keycloak \
    && docker-compose rm -f keycloak \
    && docker-compose stop keycloak_db \
    && docker-compose rm -f keycloak_db \
    && docker volume rm -f "${current_folder}_keycloak_db" \
    && docker-compose up --no-start \
    && docker-compose start keycloak_db \
    && docker cp "${data_file_path}" "$(docker-compose ps -q keycloak_db):/tmp/keycloak_data.sql" \
    && sleep 10 \
    && docker-compose exec keycloak_db bash -c "PGPASSWORD=password psql -U keycloak -w keycloak < '/tmp/keycloak_data.sql'" \
    && docker-compose up -d
