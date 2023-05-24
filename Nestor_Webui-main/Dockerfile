# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

USER root 

# Install required packages for add-on
WORKDIR /usr/src
RUN \
  apk add --no-cache \
    nginx \
    nodejs

WORKDIR /

COPY rootfs /