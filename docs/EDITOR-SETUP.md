# VS Code setup

1. Install GIANTS Farming Simulator IDE Support.
2. Keep XML formatting on save disabled if you want to preserve attribute layout.
3. Use a local absolute filesystem path for experimental schema validation, e.g.:

```xml
xsi:noNamespaceSchemaLocation="C:/MGS-FS25-Schemas/dist/fs25/vehicle.xsd"
```

4. Confirm that `interactiveControl` and `year` are recognized, and test completion within nested Interactive Control elements.
5. Restore the original schema reference before releasing a mod.

A GitHub raw URL is **not yet verified** with the GIANTS extension. Do not assume an XSD file is hosted simply because this repository exists.
