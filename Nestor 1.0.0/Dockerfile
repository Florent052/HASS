# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM 
FROM $BUILD_FROM

USER root 

# Install requirements for add-on 
WORKDIR /usr/src 
RUN \ 
  apk add --no-cache \ 
    nginx \ 
    nodejs \
    python3 \ 
    py3-pip \ 
  && pip3 install --no-cache-dir --upgrade pip\ 
    requests

WORKDIR / 


COPY rootfs /

RUN chmod 755 /usr/bin/main.py

CMD ["/usr/bin/main.py"]
