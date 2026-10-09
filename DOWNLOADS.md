# Minecraft 1.21.11 — strictly Fabric Loader 0.18.2

## [Download the real graphics-alternative pack (.mrpack)](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/download/graphics-alternative-fabric-0.18.2-1.21.11/Graphics-Alternative-1.21.11-Fabric-0.18.2-NOT-LUXIUM.mrpack)

This version is **Fabric Loader 0.18.2**, not 0.19.5. The selected mod binaries are checked by GitHub Actions for `fabric.mod.json` loader constraints, including bundled Fabric API modules.

| Component | Pinned release |
|---|---|
| Sodium | 0.8.1 (older release, not 0.8.4) |
| Iris | 1.10.3 (requires Sodium 0.8.1) |
| LambDynamicLights | 4.9.1 |
| Fabric API | 0.141.6 |
| Fabric Loader | **0.18.2** |

Install by importing the .mrpack into a **new** Modrinth-compatible launcher instance. Do NOT install .mrpack as a JAR. The original `UNIMPLEMENTED` Luxium/Embeddium JARs must be removed.

**Your Compact BedWars HUD 1.3 must also be removed** from this instance because its own metadata requires Fabric Loader 0.19.3 or newer. This pack does not include it, and no compatibility patch for that mod is supplied.

This is a functional-mod **alternative**, not a port of Luxium or Embeddium. It provides real Sodium optimization, Iris shader compatibility, and dynamic lighting. Add an actual shader pack separately. **No Minecraft client launch test has been performed.**

[See release status](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/tag/graphics-alternative-fabric-0.18.2-1.21.11).
