# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Install requests module for Python
RUN pip3 install requests==2.28.1

# Copy root filesystem
COPY rootfs /

# Make sure nestor scripts are executable
RUN chmod 755 /usr/bin/nestor-*

# Run the wrapper script
CMD ["/usr/bin/nestor-launch.sh"]