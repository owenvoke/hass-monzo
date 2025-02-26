# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com), and this project adheres to [Semantic Versioning](https://semver.org).

## Unreleased

## v0.2.0 - 2023-07-15

### Added
- Add multiple sensors (Balance, Currency, Spend Today, Total Balance)

### Changed
- Update to use Config Flow
- Update to use native OAuth via Application Credentials

## v0.1.6 - 2022-11-04

### Fixed
- Resolve OAuth token flow

## v0.1.5 - 2022-11-04

### Fixed
- Use `get_url` instead of old method to retrieve URL
- Prefer external or cloud URLs

## v0.1.4 - 2022-11-04

### Fixed
- Re-add unused required `device_discovery` parameter

## v0.1.3 - 2022-11-04

### Fixed
- Fix issue with invalid syntax

## v0.1.2 - 2022-11-04

### Fixed
- Use development `main` branch for `monzo` fork

## v0.1.1 - 2022-11-04

### Fixed
- Add missing HACS `iot_class` property
- Use forked `monzo` package

## v0.1.0 - 2022-11-04

### Changed
- Add support for HACS
- Update `monzo` to `v0.10.0`
- Use `cache_id` instead of a full path (defaults to `main`)
