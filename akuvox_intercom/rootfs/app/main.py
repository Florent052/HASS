import json
import sys
import requests


import json

def load_config():
    """Load and return the addon configuration"""
    # Load addon configuration into config
    with open("/data/options.json", "r") as config_in:
        config = json.load(config_in)

    # debug_data("CONFIGURATION", config)
    return config

def main():
    config = load_config()
    api_key = config["api_key"]
    user_id = config["user_id"]

    print(config)
    print("api_key:", api_key)
    print("user_id:", user_id)

if __name__ == "__main__":
    # Exécuter la fonction principale
    main()


# api_url = "http://adresse_de_l_api/v1/calllog"

# params = {
#     "start_date": "2023-01-01",
#     "end_date": "2023-01-31",
#     "user_id": "12345",
#     "api_key": "ta_clé_d_api",
#     "call_type": "missed"
# }

# response = requests.get(api_url, params=params)

# if response.status_code == 200:
#     call_logs = response.json()
#     phone_numbers = {}
#     for call_log in call_logs:
#         caller = call_log["caller"]
#         call_type = call_log["call_type"]
#         if call_type == "missed":
#             if caller in phone_numbers:
#                 phone_numbers[caller] += 1
#             else:
#                 phone_numbers[caller] = 1
#             # Vérifier si trois appels manqués successifs ont été effectués par le même numéro
#             if phone_numbers[caller] == 3:
#                 print(f"Urgent : Trois appels manqués successifs du numéro {caller}")
#     print(phone_numbers)
# else:
#     print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
