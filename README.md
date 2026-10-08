# MGS FS25 Schemas

A development workspace for extending Farming Simulator 25 XML schema validation and IntelliSense with community mod features.

> **Status: experimental.** Hosted XSD compatibility with GIANTS Farming Simulator IDE Support must be tested before using this as a production schema source.

## Goals

- Keep original GIANTS schema definitions unchanged.
- Maintain third-party additions separately and document their source/version.
- Generate extended XSDs reproducibly.
- Test generated schemas before publishing.
- Never modify vehicle XML files automatically.

## Initial extensions

- Interactive Control: reference documentation provided by the mod author; implementation under development.
- Vehicle Years: `vehicle/storeData/specs/year` support is provisional pending verification.

## Layout

- `extensions/` — independently documented mod-specific additions.
- `scripts/` — schema build and validation tools.
- `dist/fs25/` — generated output (not yet published).
- `docs/` — editor setup and verification.

## Local use

The project is not yet ready to supply a stable remote `vehicle.xsd` URL. Once generated output is verified and committed, use the raw URL of a pinned release or GitHub Pages endpoint. Do not reference an unverified URL in released mods.

## Rights

GIANTS' and third-party materials remain the property of their respective owners. This repository does not claim ownership or a redistribution license for upstream schemas. Keep the repository private until distribution rights are confirmed.

Maintained by MyGameSteam.
