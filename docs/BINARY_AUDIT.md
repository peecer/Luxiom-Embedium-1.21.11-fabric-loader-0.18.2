# Source binary audit

Both binaries were provided for this porting effort. They are **reference inputs** only; they were not checked into Git and they are not compatible with the target Minecraft versions.

| Binary | SHA-256 |
|---|---|
| `Luxium Let there be light-2.8.0-pre-alpha.jar` | `0530b80481b233d865ed0be55e9558562893fb48edec176d730d4789a9369469` |
| `embeddium-fabric-0.3.25+mc1.20.1.jar` | `d3206b83d14491aac9a361d99afc9a0fafed080f44994c1642e2544855c6fee7` |

The Luxium Forge metadata declares `modId=luxium`, version `2.8.0-pre-alpha`, `javafml` and a mandatory **Embeddium [0.3.31,0.4)** dependency. The uploaded Embeddium Fabric JAR declares version `0.3.25+mc1.20.1`; these are **not a compatible dependency pair**, even before changing Minecraft versions.

Luxium's `luxium.mixins.json` and Embeddium's `embeddium.mixins.json` cannot be used without porting their targets and associated Java code. The older Embeddium JAR embeds Sodium, Indium, and Fabric libraries. Do not copy this shaded bundle into these modern builds.

Embeddium is LGPL-3.0-only and requires compliance with its notices/license when importing source. Luxium is under Vinlanx's custom license; this workspace relies on the permission reported by the requester. Do not assume that permission extends to third-party redistribution.

**No original renderer, shader code, graphical assets, or decompiled bytecode has been imported yet.**
