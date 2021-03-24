# Telemeta-mshs

## Installation

### System dependencies


* Install Docker

See [Docker CE](https://docs.docker.com/install/#platform-support-matrix)

* Install tkinter

```
apt-get install python-tk python-gst-1.0 python-dev libmysqlclient-dev
```

### Git dependencies

* Clone the repository

```
git clone git@github.com:lluc/telemeta-integration.git
```

* Manage sub modules

```
git submodule update --recursive --init
```

### Run stack

> You must have docker compose installed inside a Python2 virtualenv

```
docker-compose up
```

### Run tests

We need to install tests dependencies inside container before and remove south

```
docker-compose exec app bash -c 'PYTHONPATH=telemeta_mshs/apps pip install --no-cache-dir .[tests]'
```

Now, we can launch tests
```
docker-compose exec app bash -c 'PYTHONPATH=telemeta_mshs/apps python manage.py test --settings=telemeta_mshs.settings.testing -v 3'
```

## URLs

With Traefik as reverse proxy, you can use explicit fqdn instead IP addresses.

* [Root app](http://nginx.francoralite.localhost:50000)
* [Keycloak](http://keycloak.francoralite.localhost:50000)

During development, all services are accessible behind the reverse proxy but this must be change for the production deployment.
