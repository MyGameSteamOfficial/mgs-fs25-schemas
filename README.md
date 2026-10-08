# MGS FS25 Schemas

XML schemas for Farming Simulator 25 mod development, maintained by [MyGameSteam](https://mygamesteam.com).

The collection extends the standard vehicle schema with support for community mod XML while retaining the original schema definitions for other game systems.

## Schema URL

```text
https://raw.githubusercontent.com/MyGameSteamOfficial/mgs-fs25-schemas/main/dist/fs25/vehicle.xsd
```

Add the URL to the root `vehicle` element in an XML file:

```xml
<vehicle type="car" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/MyGameSteamOfficial/mgs-fs25-schemas/main/dist/fs25/vehicle.xsd">
```

**Note:** The repository must be public for unauthenticated access. Editor support for remote schema references varies; test completion and validation in your XML extension. The URL above tracks `main` and may change as schemas are updated.

## Supported additions

- **Interactive Control:** elements and attributes documented by the Interactive Control project, including click points, animations, functions, object changes, dashboards and dependencies.
- **Vehicle Years:** support for `vehicle/storeData/specs/year`.

The Vehicle Years addition covers the year element only. Interactive Control's published reference is incomplete, so some values remain broadly typed.

## Repository

| Path | Contents |
| --- | --- |
| `dist/fs25/` | XML schemas for editor use |
| `upstream/giants/` | Original GIANTS schema files |
| `scripts/build.py` | Generates the extended schema collection |
| `extensions/` | Integration notes and source references |
| `docs/` | Editor setup |

## Build

Requires Python 3 and [lxml](https://lxml.de/).

```bash
python -m pip install lxml
python scripts/build.py
```

The builder copies the upstream schema collection and applies the vehicle extensions to the generated output. Edit the sources and builder, not the generated XSDs.

## Compatibility

These schemas assist editing and validation; they do not add functionality to Farming Simulator 25. Mods using Interactive Control or Vehicle Years still require their respective runtime mods. The schema collection has not been exhaustively tested against every vehicle configuration.

## Credits and rights

Farming Simulator and GIANTS Software are trademarks of their respective owners. The original GIANTS schema files and third-party documentation remain the property of their respective authors. MGS extensions are independently maintained and are not affiliated with or endorsed by GIANTS Software.

