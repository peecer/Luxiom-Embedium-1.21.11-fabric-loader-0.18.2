# Download the expanded Luxium-style graphics pack — Minecraft 1.21.11 / Fabric 0.18.2

**[Download the complete real graphics alternative (.mrpack)](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/download/luxium-style-fabric-0.18.2-1.21.11/Luxium-Style-Graphics-1.21.11-Fabric-0.18.2-NOT-LUXIUM.mrpack)**

Includes Sodium 0.8.1, Iris 1.10.3, LambDynamicLights 4.9.1, ImmediatelyFast 1.14.3, Cull Leaves 4.1.1.1, ModernFix-mVUS 5.25.2, Fabric API 0.141.6, required MidnightLib, and Complementary Reimagined r5.9.3 shader pack.

**IMPORTANT:** The original Luxium engine is **NOT included or ported**. This is a full *Luxium-style graphics alternative*, not a Luxium installation. Its original Forge 1.20.1-only mod cannot run on Minecraft 1.21.11/Fabric 0.18.2.

**Install:** Import this .mrpack into a clean instance in a Modrinth-compatible launcher, then enable Complementary in Iris. Keep Fabric Loader exactly 0.18.2. Do not copy over old UNIMPLEMENTED JARs or Compact BedWars HUD 1.3.

[Release and verification](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/tag/luxium-style-fabric-0.18.2-1.21.11) · [What it includes](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/blob/main/LUXIUM_STYLE_PACK.md)

---

# Minecraft 1.21.11 — Fabric Loader 0.18.2 ONLY

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

---

---

# Luxium + Embeddium — Minecraft 1.21.11 / Fabric 0.18.2

> **WORK IN PROGRESS / NO PLAYABLE RELEASE** — This GitHub repository now includes a Gradle project and compilation bootstraps, but it does **not** contain the original renderer, shaders, mixins or any functional features.

This repository has two port targets, **Luxium** (originally Forge 1.20.1 by Vinlanx) and **Embeddium** (original Fabric 1.20.1 binary supplied by the requester). Both must be ported to Minecraft 1.21.11 / Fabric 0.18.2; Java 21 is required.

## Repository contents

- `luxium/`: Fabric client-only entrypoint placeholder.
- `embeddium/`: Fabric client-only entrypoint placeholder.
- `settings.gradle` and `gradle.properties`: multi-project Gradle setup.
- `.github/workflows/gradle.yml`: compile verification on pushes and PRs.
- `docs/BINARY_AUDIT.md`: hashes, old dependency mismatch and provenance.
- `PORT_STATUS.md`: feature and validation checklist.

## Build setup

1. Install JDK 25 to run Loom (and JDK 21 as a compile toolchain) plus Gradle 9.7.0, then run `gradle build` (or generate the Gradle wrapper first).
2. Check GitHub Actions for compilation results.
3. **Do not install generated JARs as working mods.** These bootstraps only show how the mod loader can load basic entrypoints.

## Port milestones

1. Import authorized, **editable source** for Luxium and the corresponding Embeddium branch; preserve applicable copyright/license notices.
2. Port shader resources, options GUI, renderer hooks and mixin targets to 1.21.11.
3. Rework Luxium-Embeddium integration and dependency/version declarations, including the old binaries' mismatch detailed in the audit.
4. Compile, launch in Minecraft, test graphics and world loading, then prepare actual releases.

**A Gradle bootstrap is not a fork of the full implementation.** All inherited original features are currently absent.
