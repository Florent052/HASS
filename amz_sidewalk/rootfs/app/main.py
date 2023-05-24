import json
import sys
import requests
from twilio.rest import Client


def load_config():
    """Load and return the addon configuration"""
    # Load addon configuration into config
    with open("/data/options.json", "r") as config_in:
        config = json.load(config_in)

    # debug_data("CONFIGURATION", config)
    return config

def main():



    # Vos identifiants d'authentification Twilio
    account_sid = 'AC09fde8ded355d716af3e5c3749e6b121'
    auth_token = 'cf031536b2254b771a80b8cc61786b32'

    # Créer un client Twilio
    client = Client(account_sid, auth_token)

    # Envoyer le message
    message = client.messages.create(
        from_ = 'whatsapp:+12707176995',
        body = 'Hello, World!',
        to = 'whatsapp:+22964063663'
    )

    # Afficher le SID du message envoyé
    print(message.sid)

        # Call the load_config() function and print the returned configuration
        # config = load_config()
    print(load_config())

if __name__ == "__main__":
    # Run main function
    main()
    sys.exit(0)
