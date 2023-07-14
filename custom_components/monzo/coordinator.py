import logging
from datetime import timedelta

import async_timeout
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from monzo import Monzo

_LOGGER = logging.getLogger(__name__)


class MonzoUpdateCoordinator(DataUpdateCoordinator):
    """Coordinates updates between all Monzo sensors defined."""

    def __init__(
        self,
        hass: HomeAssistant,
        name: str,
        token: str,
        update_interval: timedelta,
    ) -> None:
        self._monzo: Monzo = Monzo(access_token=token)

        """Initialize the UpdateCoordinator for Monzo sensors."""
        super().__init__(
            hass,
            _LOGGER,
            name=name,
            update_interval=update_interval,
        )

    async def _async_update_data(self):
        async with async_timeout.timeout(5):
            return await self.hass.async_add_executor_job(
                lambda: self._monzo.get_balance()
            )
