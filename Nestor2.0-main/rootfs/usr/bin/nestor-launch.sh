#!/usr/bin/with-contenv bashio
# ^ The above line gets SUPERVISOR_TOKEN into our environment

# exec the script
# Running the script directly did not work reliably so instead
# we exec the python interpreter and pass the script as an argument

exec python3 /usr/bin/nestor-service.py
