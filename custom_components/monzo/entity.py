from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import STATE_UNAVAILABLE
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, SENSOR_KEY_BALANCE
from .coordinator import MonzoUpdateCoordinator


class MonzoSensorEntity(CoordinatorEntity[MonzoUpdateCoordinator], SensorEntity):
    """Representation of a Monzo sensor."""

    entity_description: SensorEntityDescription

    def __init__(
        self,
        coordinator: MonzoUpdateCoordinator,
        entry: ConfigEntry,
        description: SensorEntityDescription,
    ):
        """Initialize the sensor and set the update coordinator."""
        super().__init__(coordinator)
        self._attr_name = description.name
        self._attr_unique_id = f"{entry.entry_id}_{description.key}"

        self.entry = entry
        self.entity_description = description

    @property
    def native_value(self):
        if self.entity_description.key == SENSOR_KEY_BALANCE:
            return self.coordinator.data["balance"] / 100

        if self.entity_description.key == SENSOR_KEY_BALANCE:
            return self.coordinator.data["total_balance"] / 100

        if self.entity_description.key == SENSOR_KEY_BALANCE:
            return self.coordinator.data["currency"]

        if self.entity_description.key == SENSOR_KEY_BALANCE:
            return self.coordinator.data["spend_today"] / 100

        return STATE_UNAVAILABLE

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            name=self.coordinator.name,
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, f"{self.entry.entry_id}")},
            manufacturer="Monzo",
        )
