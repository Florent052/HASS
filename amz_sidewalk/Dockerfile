# Define build argument
ARG BUILD_FROM

FROM $BUILD_FROM

USER root

RUN apk add --no-cache python3 \ 
    py3-pip \ 
    && pip3 install --no-cache-dir --upgrade pip\
    requests\
    twilio

# Copy data for add-on
COPY rootfs /

RUN chmod a+x /app/main.py

ENTRYPOINT [ "python3", "/app/main.py" ]
