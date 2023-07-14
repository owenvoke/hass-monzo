"""Constants for the Monzo integration."""
from typing import Final

DOMAIN: Final = "monzo"

DEFAULT_SCAN_INTERVAL: Final = 120

SENSOR_KEY_BALANCE: Final = "balance"

OAUTH2_AUTHORIZE: Final = "https://auth.monzo.com"
OAUTH2_TOKEN: Final = "https://api.monzo.com/oauth2/token"
