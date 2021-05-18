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

We need to install tests dependencies inside container before run tests

```
docker-compose exec app bash -c 'pip install --no-cache-dir .[tests]'
```

Now, we can launch tests
```
docker-compose exec app bash -c 'py.test'
```

## URLs

> Replace **50000** with your Traefik listening port

With Traefik as reverse proxy, you can use explicit fqdn instead IP addresses.

* [Root app](http://nginx.francoralite.localhost:50000)
* [Keycloak](http://keycloak.francoralite.localhost:50000)

During development, all services are accessible behind the reverse proxy but this must be change for the production deployment.

### Documentation

> You **MUST** update the permission linked to these URLs

* [Redoc UI](http://nginx.francoralite.localhost:50000/redoc/)
* [Swagger UI](http://nginx.francoralite.localhost:50000/swagger/)
* [JSON Swagger export](http://nginx.francoralite.localhost:50000/swagger.json)
* [YAML Swagger export](http://nginx.francoralite.localhost:50000/swagger.yaml)
