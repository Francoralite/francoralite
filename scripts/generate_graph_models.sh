#!/bin/bash

export PYTHONPATH=$PWD/francoralite/apps:$PYTHONPATH

apt install -y python3-graphviz
pip install --prefer-binary pydotplus

django-admin graph_models francoralite_api -o models_api.png
django-admin graph_models francoralite_api -o models_api.svg
django-admin graph_models -a -g -o models_all.png
django-admin graph_models -a -g -o models_all.svg
