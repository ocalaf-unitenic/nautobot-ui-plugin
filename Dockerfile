ARG FROM_IMAGE=netboxcommunity/netbox
ARG FROM_TAG=latest-ldap
ARG FROM=${FROM_IMAGE}:${FROM_TAG}
FROM ${FROM}

ENV VIRTUAL_ENV=/opt/netbox/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY ./nextbox_ui_plugin_docker /source/nextbox-ui-plugin_docker/nextbox_ui_plugin_docker/
COPY ./setup.py /source/nextbox-ui-plugin_docker/
COPY ./MANIFEST.in /source/nextbox-ui-plugin_docker/
COPY ./README.md /source/nextbox-ui-plugin_docker/
COPY --chown=1000:1000 --chmod=644 ./nextbox_ui_plugin_docker/static/nextbox_ui_plugin_docker /opt/netbox/netbox/static/nextbox_ui_plugin_docker
RUN pip3 install --no-cache-dir nextbox-ui-plugin-docker
