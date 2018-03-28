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
git submodule init && git submodule update
```

### Python dependencies

* Install Python dependencies (inside a virtualenv)

```
pip install -r requirements.txt
```

### Run stack

```
docker-compose up
```

### Run tests

```
docker-compose exec app bash -c 'PYTHONPATH=telemeta_mshs/apps python manage.py test --settings=telemeta_mshs.settings.testing -v 3'
```
