"""Capteur pour le module d'intégration Amazon Sidewalk."""
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import ATTR_ATTRIBUTION

from .const import DOMAIN, ATTRIBUTION

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([AmazonSidewalkSensor(entry)], True)

class AmazonSidewalkSensor(SensorEntity):
    def __init__(self, entry):
        self._entry = entry
        self._name = f"{DOMAIN}_sensor"
        self._state = None
        self._attributes = {}

    async def async_update(self):
        self._state = 0
        self._attributes = {ATTR_ATTRIBUTION: ATTRIBUTION}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def device_state_attributes(self):
        return self._attributes
