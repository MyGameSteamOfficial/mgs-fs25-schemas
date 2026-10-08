# Vehicle schema extensions

`scripts/build.py` generates `dist/fs25/vehicle.xsd` from `upstream/giants/vehicle.xsd`.

The current additions cover Interactive Control elements and the `storeData/specs/year` element used by Vehicle Years.

Interactive Control definitions are based on the supplied project reference; some constraints are intentionally permissive where the reference does not specify valid values. Changes should be checked against representative vehicle XML before release.

The schema describes valid XML structure. Minimal XML insertion templates are maintained separately in the MGS editor extension.
