# CurseForge modpack export — Luxiom development fork included

[Download the ZIP from GitHub Releases](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/tag/curseforge-dev-0.1.0-mc1.21.11-fabric0.18.2)

This is a standard CurseForge-import format: `manifest.json` and `overrides/` in a ZIP.

Target is **Minecraft 1.21.11 with Fabric Loader 0.18.2**. Includes genuine CurseForge projects for Sodium 0.8.1, Iris 1.10.3, Fabric API 0.141.6, LambDynamicLights 4.9.1, ImmediatelyFast 1.14.3, Cull Leaves 4.1.1.1, MidnightLib 1.9.3, ModernFix-mVUS 5.25.2, and Complementary Reimagined r5.9.3.

The `overrides/mods` directory contains **our Luxium development fork JAR**. Its SHA-256 is `966e9da22fa06449fe9d19b038013a42b4f1f217ce1a4ac8358480efabfe8e70`, and its `fabric.mod.json` declares Luxium `0.0.0-dev`.

**Its feature status is NOT IMPLEMENTED:** the current Luxium fork has no working lighting, shaders, LSR, TFR, or original rendering integrations. This pack installs the Luxium fork file but cannot enable features that have not been ported.

The duplicate-id Embeddium placeholder is intentionally excluded to avoid conflicts with Sodium. Avoid Compact BedWars HUD 1.3 on this loader.

To import, select the release ZIP through CurseForge Minecraft **Import Profile** as a NEW instance. This import has not been tested in the CurseForge app.

For public CurseForge publication, the pack's override JAR must meet CurseForge's third-party mod inclusion rules, which can require approved licensing and review. The GitHub ZIP is provided for private developer testing, not as an accepted public CurseForge project.

Build source: [workflow](.github/workflows/curseforge-dev-pack.yml) and [manifest](curseforge/manifest.json).
