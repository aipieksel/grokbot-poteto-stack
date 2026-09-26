# Usage

Keep the package separate from the project that will use it. Install the entire skill folder once; seed context once per project:

```sh
./scripts/seed-os.sh /path/to/project
```

The target project must exist. The helper creates `operating-system/` and refuses overwrite. There is no destructive reset flag. Fill in `context/goals.md`, `projects.md`, `preferences.md`, and `trusted-sources.md`. The JSON memory and task files begin as empty arrays, ready for your own dated records.

Load [SKILL.md](SKILL.md), read the project context, then try one [job packet](docs/JOB-PACKETS.md) and verify the returned evidence before considering recurring automation. Adapters are instructions, not installed integrations. See [getting started](docs/GETTING-STARTED.md).
