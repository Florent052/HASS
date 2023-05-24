#!/usr/bin/env python3

import json
import os
import sys
import time

import requests

# URL to post registration data to
REGISTRATION_URL = "https://webhook.site/06255c6f-30ae-4b14-8502-cf0fae4e6d65"

# Home Assistant API URL to retrieve history from
# Defaults to returning 1 day of history
HISTORY_URL = "http://supervisor/core/api/history/period"

# Home Assistant API URL to retrieve lobook from
# Defaults to returning 1 day of logbook
LOGBOOK_URL = "http://supervisor/core/api/logbook"

# Headers for request to Home Assistant API
# Needs SUPERVISOR_TOKEN from environment for authorization
HASSIO_HEADERS = {"Authorization": f"Bearer {os.environ['SUPERVISOR_TOKEN']}"}


def debug_data(title, data):
    """Debugging function to print a data structure to the addon log"""
    sys.stderr.write(f"{title}:\n")
    json.dump(data, sys.stderr, indent=2, sort_keys=True)
    sys.stderr.write("\n")


def load_config():
    """Load and return the addon configuration"""
    # Load addon configuration into config
    with open("/data/options.json", "r") as config_in:
        config = json.load(config_in)

    debug_data("CONFIGURATION", config)
    return config


def post_data(url, data):
    """Post data to a URL; raises exception on error"""

    response = requests.post(url, json=data)
    # Raise error if request failed
    response.raise_for_status()

    return response


def get_data(url):
    """Retrieve data from Home Assistant API using auth token"""

    response = requests.get(url, headers=HASSIO_HEADERS)
    # Raise error if request failed
    response.raise_for_status()

    return response


def main():
    """Main function of program"""

    # Load addon config and post to REGISTRATION_URL
    config = load_config()
    post_data(REGISTRATION_URL, config)

    sys.stderr.write("Waiting for input...\n")
    # Read lines of input
    # These will come from the hassio.addon_stdin service
    # Every time the hassio.addon_stdin service is called for our addon,
    # we will get a line of input.
    for line in sys.stdin:
        # Retrieve last 24 hours of history and logbook from Home Assistant
        history = get_data(HISTORY_URL)
        logbook = get_data(LOGBOOK_URL)

        # Create dictionary with message, history, and logbook
        event = {
            "message": line.strip(),
            "history": history.json(),
            "logbook": logbook.json()
        }

        sys.stderr.write(f"Got input: {event['message']}\n")

        # Post event to REGISTRATION_URL
        response = post_data(REGISTRATION_URL, event)
        sys.stderr.write(f"Sent event to {REGISTRATION_URL}: {response.status_code}\n")

    sys.stderr.write("No more input, exiting...\n")


if __name__ == "__main__":
    # Run main function
    main()
    sys.exit(0)
