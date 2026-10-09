# Important: the previous JAR releases are NOT functional Minecraft mods

# Real graphics alternative for Minecraft 1.21.11

## What this actually does
The **old UNIMPLEMENTED .jar downloads are not playable mods**, and they cannot be made working by editing `fabric.mod.json`. They were empty entrypoint prototypes and must be **removed** from your Minecraft mods folder.

**The correct solution for the original screenshot:** install Fabric Loader **0.19.5 or later**, remove the stub Embeddium JAR that conflicts with Sodium, and use real graphics mods. Compact BedWars HUD 1.3 requires 0.19.3+, and Sodium 0.8.4 requires 0.19.5+.

## [Download graphics alternative (.mrpack)](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/download/graphics-alternative-0.2-1.21.11/Graphics-Alternative-1.21.11-Fabric-0.19.5-NOT-LUXIUM.mrpack)

You can also visit the [alternative release page](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/tag/graphics-alternative-0.2-1.21.11).

This is a **new, clean modpack**, NOT a fork or port of Luxium or Embeddium. It uses genuine **Sodium (rendering/performance), Iris (shader pack compatibility), LambDynamicLights (dynamic lights), and Fabric API**, with required dependencies chosen from official Modrinth version metadata. It does not bundle the actual .jar files: the compatible launcher downloads verified files from Modrinth.

Import the .mrpack into a Modrinth-format pack launcher, create a **separate instance**, then add an optional shader pack. Do not copy your original mods folder over without checking compatibility. The exact Iris/Sodium pairing is selected from dependencies to avoid known version conflicts.

**Status:** The pack generator and automatic checks validate metadata and version dependencies; no claim of in-game testing. No real Luxium feature code is contained here.

For Forge 26.2, see [Forge alternative](https://github.com/peecer/Luxiom-Embedium-26.2-Forge-65.1.0/blob/main/WORKING_ALTERNATIVE.md).

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
