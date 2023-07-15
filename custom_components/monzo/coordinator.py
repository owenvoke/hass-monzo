from __future__ import annotations

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
        self._monzo: Monzo | None = None
        self._account_id: str | None = None
        self._session: OAuth2Session = session
        self._entry: ConfigEntry = entry

        self.refresh_monzo_instance()

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=DEFAULT_UPDATE_INTERVAL,
        )

    def refresh_monzo_instance(self) -> None:
        self._monzo: Monzo = Monzo(access_token=self._session.token["access_token"])

    async def _async_update_data(self):
        async with async_timeout.timeout(5):
            token = self._session.token["access_token"]

            await self.hass.async_add_executor_job(
                lambda: self._session.async_ensure_token_valid()
            )

            if token != self._session.token["access_token"]:
                self.refresh_monzo_instance()

            if self._account_id is None:
                account = await self.hass.async_add_executor_job(
                    lambda: self._monzo.get_first_account()
                )

                self._account_id = account["id"]

            if self._account_id is None:
                raise MonzoAccountError("No account id was configured.")

            return await self.hass.async_add_executor_job(
                lambda: self._monzo.get_balance(self._account_id)
            )


class MonzoAccountError(Exception):
    pass
