#!/usr/bin/env bash


# Constants
REPOSITORY=francoralite/francoralite
COMMIT_SHORT=${TRAVIS_COMMIT::8}


# Variables


# Build image
docker build -t "${REPOSITORY}:${COMMIT_SHORT}" .


# Create tags
if [[ "${TRAVIS_TAG}" != "" ]];
then
    docker tag "${REPOSITORY}:${COMMIT_SHORT}" "${REPOSITORY}:${TRAVIS_TAG}"
elif [[ "${TRAVIS_BRANCH}" == "master" ]];
then
    docker tag "${REPOSITORY}:${COMMIT_SHORT}" "${REPOSITORY}:latest"
fi
docker tag "${REPOSITORY}:${COMMIT_SHORT}" "${REPOSITORY}:travis-${TRAVIS_BUILD_NUMBER}"


# Push image
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USER" --password-stdin
docker push "${REPOSITORY}"
