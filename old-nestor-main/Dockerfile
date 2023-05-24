# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
#ARG TEMPIO_VERSION BUILD_ARCH
#RUN \
#    curl -sSLf -o /usr/bin/tempio \
#    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"
#
#RUN apk add --no-cache python3 py3-pip py3-requests

RUN pip3 install requests==2.28.1
# Copy root filesystem
COPY rootfs /

CMD ["/usr/bin/nestor-service.py"]
