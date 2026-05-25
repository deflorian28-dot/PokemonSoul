# pokeemerald-expansion AI Agent Guide

## What this repository is
- A GBA ROM hack base built on top of the `pret/pokeemerald` decompilation.
- Written in C, ARM assembly, and build scripts.
- Not a standalone playable game; it is a development framework for Pokémon ROM hacks.

## Recommended entry points
- `README.md` — project overview and high-level links.
- `INSTALL.md` — canonical build and toolchain instructions.
- `CONTRIBUTING.md` — PR flow, branch guidance, and issue/report expectations.
- `docs/STYLEGUIDE.md` — coding conventions for this project.
- `docs/tutorials/how_to_testing_system.md` — how to run and author automated tests.

## Build and test commands
- `make` — build the default ROM target.
- `make debug` — build debug symbols with `pokeemerald.elf`.
- `make release` — build a release-optimized ROM.
- `make check -j` — run the automated test suite in parallel.
- `make check TESTS="..."` — run a focused subset of test names.
- `make pokeemerald-test.elf TESTS="..."` — build a test ROM for interactive debugging.
- `make TOOLCHAIN="/path/to/toolchain"` — override the ARM toolchain path.

## Repository structure
- `src/` — main C source code.
- `asm/` — ARM assembly sources and macros.
- `data/` — data tables, scripts, maps, and assets.
- `include/` — project headers.
- `build/` — generated build artifacts.
- `test/` — automated test definitions.
- `tools/` — helper tools used during build.

## Style and conventions
- C and header files use 4 spaces, not tabs.
- Assembly `.s` and script `.inc` files use tabs.
- Functions and structs: `PascalCase`.
- Variables and struct fields: `camelCase`.
- Global variables: prefix `g`.
- Static variables: prefix `s`.
- Macros/constants: `CAPS_WITH_UNDERSCORES`.
- Comments should explain *why* and use `//` with one space.

## Important repository-specific details
- `Makefile` has special build options: `COMPARE`, `TEST`, `ANALYZE`, `DEBUG`, `LTO`, `UNUSED_ERROR`, `DEPRECATED_ERROR`, and `RELEASE`.
- `make check` runs the ROM testing system, which is battle-oriented and observable-output driven.
- Tests are written to prefer player-visible outputs rather than internal state.
- Use `TESTS="..."` to run groups of tests by matching prefixes.

## Branch guidance
- `master` is used for bugfixes, documentation, and tests.
- `upcoming` is used for new features.
- Consult `CONTRIBUTING.md` before proposing a large feature or branch workflow.

## How AI agents should behave
- Prefer linking to existing docs instead of repeating details.
- Preserve existing repository conventions and naming when adding code.
- Avoid suggesting changes that require a playable game build from scratch; this repo is a ROM hack base.
- For code changes, verify with `make` and `make check` whenever feasible.

## Useful quick links
- [README.md](README.md)
- [INSTALL.md](INSTALL.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/STYLEGUIDE.md](docs/STYLEGUIDE.md)
- [docs/tutorials/how_to_testing_system.md](docs/tutorials/how_to_testing_system.md)
