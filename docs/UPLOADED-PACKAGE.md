# Supplied schema package

The uploaded archive `MGS-FS25-Schemas.zip` contains 188 ZIP entries, including `upstream/giants/`, `dist/fs25/`, `scripts/build.py`, `extensions/interactive-control-reference.md`, and `snippets/fs25.code-snippets`.

The supplied builder copies GIANTS schemas then patches `vehicle.xsd` with Interactive Control definitions and provisional Vehicle Years `specs/year` support.

**Important:** The uploaded XSD collection is not yet committed here. No remote `dist/fs25/vehicle.xsd` is available. Do not point editor configuration to a nonexistent GitHub raw URL.

Before public distribution: verify source permissions, validate all generated XSDs, and test schema loading from a remote URL in VS Code.
