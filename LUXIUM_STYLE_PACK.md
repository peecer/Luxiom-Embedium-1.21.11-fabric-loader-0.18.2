# Luxium-style full graphics alternative — Minecraft 1.21.11 / Fabric 0.18.2

**This project is NOT the original Luxium mod or a working Luxium port.**

Luxium's only official binary is for **Forge 1.20.1**, requiring **Embeddium 0.3.31–0.3.x**. Its shader pipeline has 46 old mixins and cannot run unchanged on Fabric 1.21.11. Do not add either the old Forge Luxium JAR or any of the previous UNIMPLEMENTED placeholder JARs to the modpack.

## Included in the extended pack

- Sodium 0.8.1 — modern chunk rendering and optimization.
- Iris 1.10.3 — shader-pack support, paired to its pinned Sodium version.
- LambDynamicLights 4.9.1 — dynamic light sources.
- Fabric API 0.141.6 and selected required dependencies.
- ImmediatelyFast 1.14.3 — optimized immediate rendering.
- Cull Leaves 4.1.1.1 — more efficient leaf rendering.
- ModernFix-mVUS 5.25.2 — additional optimization and fixes.
- Complementary Reimagined — external official shader ZIP selected for 1.21.11; enable via Iris settings.

The GitHub Actions generator verifies hashes, binary Fabric Loader requirements (including bundled modules), required dependencies and a valid shader ZIP before publishing. **Loader remains exactly 0.18.2.** There is no game-launch test.

[View the validated pack release](https://github.com/peecer/Luxiom-Embedium-1.21.11-fabric-loader-0.18.2/releases/tag/luxium-style-fabric-0.18.2-1.21.11).

Import the `.mrpack` file as a **separate clean instance** in a compatible launcher; it is not a JAR. Do not add Compact BedWars HUD 1.3, which requires Fabric Loader 0.19.3 or newer.

## What is still missing from Luxium

The actual Luxium renderer and its special effects (such as Luxium Spatial Resolution and Temporal Frame Reprojection) are not implemented. Porting them requires the original editable Luxium code/assets or a reconstruction from the binary, then adapting its Forge/Embeddium hooks to Fabric 1.21.11 and testing in the Minecraft client. The shader pack offers similar visuals, not feature or performance equivalence.
