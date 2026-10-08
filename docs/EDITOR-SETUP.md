# Editor setup

For VS Code, install an XML extension with XSD support and open the mod folder as a workspace.

Reference the hosted vehicle schema in the XML root element:

```xml
<vehicle type="car" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/MyGameSteamOfficial/mgs-fs25-schemas/main/dist/fs25/vehicle.xsd">
```

The GitHub repository must be public for the URL to work without authentication. Some editor extensions only resolve local schema paths; if remote resolution fails, download the schema directory and reference its local `vehicle.xsd`.

Avoid changing schema references in released mod XML unless the target game and mod distribution process explicitly supports that reference.
