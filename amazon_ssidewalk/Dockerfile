ARG BUILD_FROM
FROM $BUILD_FROM

# Set the working directory to the app directory
WORKDIR /app

# Install dependencies
RUN pip3 install -r requirements.txt
RUN apk add --no-cache python3 py3-pip
RUN pip3 install homeassistant

# Copy the module files
COPY . /app/

# Start Home Assistant and run the module
CMD [ "python3", "-m", "homeassistant", "--config", "/config", "--verbose", "--debug", "-c", "/app" ]
