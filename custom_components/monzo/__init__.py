"""The Monzo integration"""
import logging

import aiohttp
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady, ConfigEntryAuthFailed
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers.config_entry_oauth2_flow import (
    async_get_config_entry_implementation,
    OAuth2Session,
)

from . import config_flow
from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL
from .coordinator import MonzoUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up Monzo integration."""
    hass.data[DOMAIN] = {}

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    implementation = await async_get_config_entry_implementation(hass, entry)

    session = OAuth2Session(hass, entry, implementation)

    try:
        await session.async_ensure_token_valid()
    except aiohttp.ClientResponseError as err:
        _LOGGER.debug("API error: %s (%s)", err.status, err.message)
        if err.status in (401, 403):
            raise ConfigEntryAuthFailed("Token not valid, trigger renewal") from err
        raise ConfigEntryNotReady from err

    monzo_coordinator = MonzoUpdateCoordinator(hass=hass, entry=entry, session=session)

    await monzo_coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = monzo_coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
