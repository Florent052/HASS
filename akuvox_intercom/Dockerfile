# Define build argument
ARG BUILD_FROM

FROM $BUILD_FROM

# Installation des paquets nécessaires
RUN apk update \
    && apk add --no-cache python3 py3-pip \
    && pip3 install --no-cache-dir --upgrade pip requests

# Copie des fichiers de l'add-on
COPY rootfs /

# Attribution des permissions d'exécution au script principal
RUN chmod a+x /app/main.py

# Point d'entrée de l'application
ENTRYPOINT [ "python3", "/app/main.py" ]
