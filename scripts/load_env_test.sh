#!/bin/bash
docker-compose exec app bash -c 'pip install --no-cache-dir .[tests]'
docker-compose exec app bash -c './scripts/deps_selenium.sh'
