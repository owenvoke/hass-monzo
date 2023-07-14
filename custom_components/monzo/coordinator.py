import logging

import async_timeout
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from monzo import Monzo

from custom_components.monzo import DOMAIN, DEFAULT_UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)


class MonzoUpdateCoordinator(DataUpdateCoordinator):
    """Coordinates updates between all Monzo sensors defined."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
        session: OAuth2Session,
    ) -> None:
        """Initialize the UpdateCoordinator for Monzo sensors."""
        self._session: OAuth2Session = session
        self._entry: ConfigEntry = entry

        self._monzo: Monzo = Monzo(access_token=session.token["access_token"])

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=DEFAULT_UPDATE_INTERVAL,
        )

    async def _async_update_data(self):
        async with async_timeout.timeout(5):
            account = await self.hass.async_add_executor_job(
                lambda: self._monzo.get_first_account()
            )

            return await self.hass.async_add_executor_job(
                lambda: self._monzo.get_balance(account["id"])
            )
