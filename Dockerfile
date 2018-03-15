FROM parisson/timeside:latest-dev

#RUN apt-get update && apt-get install -y python-tk python-gst0.10


ENV PYTHON_EGG_CACHE=/srv/.python-eggs
RUN mkdir -p /srv/src/.python-eggs
RUN chown www-data:www-data $PYTHON_EGG_CACHE

COPY requirements.txt ./
COPY ./telemeta_mshs/settings/base.py ./settings.py
COPY ./telemeta_mshs/apps/Telemeta/app/settings.py ./telemeta.py
RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall -y South

COPY . .

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["./scripts/start_api.sh"]
