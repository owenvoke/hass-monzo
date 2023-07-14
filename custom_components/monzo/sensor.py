import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import MonzoUpdateCoordinator
from .entity import MonzoSensorEntity
from .const import (
    SENSOR_KEY_BALANCE,
)

DOMAIN = "tier"

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

SCAN_INTERVAL = timedelta(minutes=5)

SENSORS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=SENSOR_KEY_BALANCE,
        name="Balance",
        icon="mdi:credit-card",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up all sensors for this entry."""
    coordinator: MonzoUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        MonzoSensorEntity(coordinator, entry, description) for description in SENSORS
    )
