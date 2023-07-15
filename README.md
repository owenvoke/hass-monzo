# HASS Monzo

[![Latest Version][ico-version]][link-releases]
[![Software License][ico-license]](LICENSE.md)
[![Build Status][ico-github-actions]][link-github-actions]
[![Buy us a tree][ico-treeware-gifting]][link-treeware-gifting]

A [Monzo](https://monzo.com) sensor for Home Assistant

## Install

### Via HACS

1. Install the [Home Assistant Community Store (HACS)](https://hacs.xyz/docs/setup/download)
2. Add Monzo as a custom repository. See [the HACS FAQs](https://hacs.xyz/docs/faq/custom_repositories) and
   add `https://github.com/owenvoke/hass-monzo`
3. Select `integration` as the category
4. You should now be able to install Monzo via HACS
5. Once installation is complete, restart Home Assistant
6. In the HA UI, go to `Configuration -> Integrations`, click `+` and search for `Monzo`

### Manual

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`)
2. If you do not have a `custom_components` directory there, you need to create it
3. Add the `monzo` directory and its contents from this repository to the `custom_components` directory in your Home
   Assistant configuration directory
4. Restart Home Assistant
5. In the HA UI, go to `Configuration -> Integrations`, click `+` and search for `Monzo`

### Dependencies

This component relies on [my fork](https://github.com/owenvoke/monzo-python-sdk) of
the [monzo](https://github.com/adesnmi/monzo-python) Python package, an unofficial client for the Monzo API.

### Usage

This can be configured fully via the Integrations interface. Click the following link to add a new Monzo user.

[![Add Integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=monzo)

To get a client ID and secret go to [the Monzo developer site](https://developers.monzo.com/apps/home) and
click `+ New OAuth Client`. Ensure you have set the confidentiality to "Confidential", and set the redirect URL
to `https://my.home-assistant.io/redirect/oauth`.

If you want to use the sensor with multiple accounts ensure you have added all the users to the "collaborators" in the
OAuth client registration with Monzo.

## Security

If you discover any security related issues, please email security@voke.dev instead of using the issue tracker.

## Credits

- [Owen Voke][link-author]
- [All Contributors][link-contributors]

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

## Treeware

You're free to use this package, but if it makes it to your production environment please consider buying the world a tree.

It’s now common knowledge that one of the best tools to tackle the climate crisis and keep our temperatures from rising above 1.5C is to plant trees. If you support this package and contribute to the Treeware forest you’ll be creating employment for local families and restoring wildlife habitats.

You can buy trees [here][link-treeware-gifting].

Read more about Treeware at [treeware.earth][link-treeware].

[ico-version]: https://img.shields.io/github/v/release/owenvoke/hass-monzo.svg?style=flat-square&sort=semver
[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
[ico-github-actions]: https://img.shields.io/github/actions/workflow/status/owenvoke/hass-monzo/tests.yml?branch=main&style=flat-square
[ico-treeware-gifting]: https://img.shields.io/badge/Treeware-%F0%9F%8C%B3-lightgreen?style=flat-square

[link-releases]: https://github.com/owenvoke/hass-monzo/releases
[link-github-actions]: https://github.com/owenvoke/hass-monzo/actions
[link-treeware]: https://treeware.earth
[link-treeware-gifting]: https://monzo.com/owenvoke?gift-trees
[link-author]: https://github.com/owenvoke
[link-contributors]: ../../contributors
