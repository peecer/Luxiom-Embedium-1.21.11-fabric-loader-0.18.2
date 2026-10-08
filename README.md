# Luxium + Embeddium port — Minecraft 1.21.11 (Fabric 0.18.2)

> **Development status: not a playable mod.** This repository is an authorized port workspace initialized from the supplied 1.20.1 binary releases. No rendering or lighting features are implemented here yet.

## Target

- Minecraft Java Edition: **1.21.11**
- Mod loader: **Fabric 0.18.2**
- Components to port: Luxium (lighting/rendering features), Embeddium (rendering optimization and interoperability)

## Original inputs

- `Luxium Let there be light-2.8.0-pre-alpha.jar` (compiled older Forge mod)
- `embeddium-fabric-0.3.25+mc1.20.1.jar` (compiled Fabric 1.20.1 mod)

The input JARs are reference binaries, not editable source projects. They are intentionally not committed. Retain upstream copyright notices and license text when importing actual source code.

## Work required

1. Obtain/import authorized source for Luxium, including shader assets and mixins; obtain appropriate Embeddium source and notices.
2. Initialize and validate the Fabric 0.18.2 development toolchain for Minecraft 1.21.11.
3. Port Minecraft rendering and shader integration, removing obsolete 1.20.1 calls and mixin targets.
4. Adapt Luxium-to-Embeddium integration; verify whether newer Sodium/Embeddium APIs provide the necessary extension points.
5. Run a clean compilation, launch the client, verify graphics, and test world loading/performance.
6. Only publish release JARs after these tests pass.

## Current state

See [PORT_STATUS.md](PORT_STATUS.md). No claim of build success or game compatibility is made.
