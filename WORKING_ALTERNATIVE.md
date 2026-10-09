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
