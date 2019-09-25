FROM parisson/timeside:latest-dev

ENV KEYCLOAK_DEFAULT_ACCESS ALLOW
ENV KEYCLOAK_REALM francoralite
ENV KEYCLOAK_SERVER_URL http://keycloak.francoralite.localhost:50000/auth/
ENV KEYCLOAK_METHOD_VALIDATE_TOKEN DECODE
ENV KEYCLOAK_CLIENT_PUBLIC_KEY abcd123
ENV KEYCLOAK_CLIENT_ID francoralite
ENV KEYCLOAK_CLIENT_SECRET_KEY abc123
ENV KEYCLOAK_AUTHORIZATION_CONFIG /tmp/authorization_config.json


ENV PYTHON_EGG_CACHE=/srv/.python-eggs
RUN mkdir -p /srv/src/.python-eggs
RUN chown www-data:www-data $PYTHON_EGG_CACHE

ADD . / ./
COPY ./telemeta_mshs/settings/base.py ./settings.py
COPY ./telemeta_mshs/apps/Telemeta/app/settings.py ./telemeta.py
RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall -y South

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["./scripts/start_api.sh"]
