import logging

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .coordinator import MonzoUpdateCoordinator
from .const import (
    SENSOR_KEY_BALANCE,
    DOMAIN,
    SENSOR_KEY_TOTAL_BALANCE,
    SENSOR_KEY_CURRENCY,
    SENSOR_KEY_SPEND_TODAY,
)
from .entity import MonzoSensorEntity

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

SENSORS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=SENSOR_KEY_BALANCE,
        name="Balance",
        icon="mdi:piggy-bank-outline",
    ),
    SensorEntityDescription(
        key=SENSOR_KEY_TOTAL_BALANCE,
        name="Total Balance",
        icon="mdi:piggy-bank",
    ),
    SensorEntityDescription(
        key=SENSOR_KEY_CURRENCY,
        name="Currency",
        icon="mdi:cash",
    ),
    SensorEntityDescription(
        key=SENSOR_KEY_SPEND_TODAY,
        name="Spend Today",
        icon="mdi:bank-transfer-out",
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
