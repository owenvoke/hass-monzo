"""Constants for the Monzo integration."""
from datetime import timedelta
from typing import Final

DOMAIN: Final = "monzo"

DEFAULT_UPDATE_INTERVAL: Final = timedelta(hours=1)

SENSOR_KEY_BALANCE: Final = "balance"
SENSOR_KEY_TOTAL_BALANCE: Final = "total_balance"
SENSOR_KEY_CURRENCY: Final = "currency"
SENSOR_KEY_SPEND_TODAY: Final = "spend_today"

OAUTH2_AUTHORIZE: Final = "https://auth.monzo.com"
OAUTH2_TOKEN: Final = "https://api.monzo.com/oauth2/token"
