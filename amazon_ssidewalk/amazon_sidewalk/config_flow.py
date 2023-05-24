"""Assistant de configuration pour le module d'intégration Amazon Sidewalk."""
import logging

import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Définition du schéma de configuration
class AmazonSidewalkConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
