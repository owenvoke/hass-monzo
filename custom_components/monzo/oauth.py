"""OAuth2 functions and classes for Monzo API integration."""
from __future__ import annotations

from typing import Any

from homeassistant.components.application_credentials import (
    AuthImplementation,
    AuthorizationServer,
    ClientCredential,
)
from homeassistant.core import HomeAssistant

from .const import OAUTH2_AUTHORIZE, OAUTH2_TOKEN


class MonzoOAuth2Implementation(AuthImplementation):
    """Local OAuth2 implementation for Monzo."""

    @property
    def extra_authorize_data(self) -> dict:
        """Extra data that needs to be appended to the authorization URL."""
        return {"scope": "*", "response_type": "code"}

    async def async_resolve_external_data(self, external_data: Any) -> dict:
        """Initialize local Monzo API auth implementation."""
        redirect_uri = external_data["state"]["redirect_uri"]
        data = {
            "grant_type": "authorization_code",
            "code": external_data["code"],
            "redirect_uri": redirect_uri,
        }

        return await self._token_request(data)

    async def _async_refresh_token(self, token: dict) -> dict:
        """Refresh tokens."""
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": token["refresh_token"],
        }

        new_token = await self._token_request(data)
        return {**token, **new_token}
