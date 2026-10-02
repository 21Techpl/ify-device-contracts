# IFY Device Contracts

Cross-app device contract for all IFY applications (web, commerce, android, iOS).
Vendor-neutral schema of the devices the apps control (WLED, Tasmota), versioned and vendored.

## Layout
- `schemas/` — JSON schemas (device capability contract)
- `wled/` — WLED JSON API notes + typed models
- `tasmota/` — Tasmota HTTP API notes + typed models
- `VERSION` — contract version, single source of truth

## Rules
- Apps **vendor** a pinned contract version; breaking changes bump the major version.
- Contract changes require a PR + human merge.
