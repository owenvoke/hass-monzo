# HASS Monzo

A Monzo sensor for Home Assistant.

## Installation

Add the `monzo` folder and its contents to the `custom_components` folder in your Home Assistant configuration directory, and add the `monzo` component to your `configuration.yaml` file.

### Example `configuration.yaml` entry

```yml
sensor:
  - platform: monzo
    client_id: !secret monzo_client_id
    client_secret: !secret monzo_client_secret
    name: 'Optional name for the sensor'
    current_account: true # Only if you use the current account
    cache_id: 'account_1' # Only if using multiple accounts (default is "main")
```

Set `current_account` to `true` only if you have a Monzo current account.

To get a client ID and secret go to [the Monzo developer site](https://developers.monzo.com/apps/home) and click `+ New OAuth Client`. Ensure you have set the confidentiality to "Confidential", and set the redirect URL to `http://ip-of-hass:8123/api/monzo`.

If you want to use the sensor with multiple accounts ensure you have added all the users to the "collaborators" in the OAuth client registration with Monzo.

### Dependencies

This component relies on the [monzo](https://github.com/adesnmi/monzo-python) Python package, an unofficial client for the Monzo API.

## Usage

With this custom component loaded, a sensor is available with your current balance.
