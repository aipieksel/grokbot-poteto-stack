# GrokBot Poteto Stack

Maintained by [aipieksel](https://github.com/aipieksel).

A portable operator workflow with named specialists, evidence-based handoffs, and per-project context on disk. This package supplies instructions and local templates; it does not provision bots, install connectors, or call paid APIs.

## Start

Python 3.10+ and a POSIX shell are required for the helpers. From this package:

```sh
./scripts/install-check.sh
./scripts/seed-os.sh /path/to/your/project
```

Seeding creates `operating-system/` inside an existing project directory. It refuses an existing destination, including symlinks, so it cannot reset your notes. Edit the seeded context files before using them. Keep credentials outside this folder.

Install the entire folder in your assistant's skill directory, preserving [SKILL.md](SKILL.md) and its relative references. Load the skill with your project path. Only use specialist, browser, or external-action capabilities actually available and authorized in that session.

## Contents

- [Getting started](docs/GETTING-STARTED.md), [architecture](docs/ARCHITECTURE.md), and [usage](USAGE.md).
- [Team roles](docs/GROK-BOT-TEAM.md), [job packets](docs/JOB-PACKETS.md), and [approval boundaries](docs/APPROVAL-GATES.md).
- [Trust curve](docs/TRUST-CURVE.md) and [Cursor adapter](adapters/cursor-pstack.md).
- [Grok Bot](adapters/grok-bot.md), [Codex](adapters/codex.md), [Grok CLI](adapters/grok-cli.md), and [ChatGPT](adapters/chatgpt.md) instruction adapters.
- [Fleet hire kit](FLEET-HIRE-KIT.md) and [optional Kimi notes](docs/OPTIONAL-KIMI.md).

## Verification

`./scripts/install-check.sh` validates shipped templates and local document links. `python3 -m unittest discover -s tests -v` checks fresh seeding and refusal to overwrite existing files or follow destination symlinks. These checks do not establish that a model follows the workflow or that a third-party integration is available.

## Credits and rights

Lauren Tan (@poteto) is credited for the pstack/trust-curve and Grok Bot team patterns described in the source notes. Alex (@de1lymoon) is credited for the optional operator/specialist disk-context pattern. These are attributed background claims, not an endorsement or verified API contract. The package is independently maintained by aipieksel. aipieksel packaging is licensed under [MIT](LICENSE). Poteto/pstack attribution remains; that credit is not a claim of authorship of upstream writing.
