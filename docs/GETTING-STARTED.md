# Getting started

1. Run `./scripts/install-check.sh` from the package.
2. Run `./scripts/seed-os.sh /path/to/project` against an existing local project.
3. Fill in the generated context files. Install this entire package in your assistant's supported skill directory, or attach [the operator instructions](../SKILL.md) with the context they reference.
4. Choose one coordinator and, if needed, a specialist named Scout. Send a bounded [job packet](JOB-PACKETS.md); a role name alone does not create an agent.
5. Inspect the evidence, record the decision, and follow the current user's authorization before acting.
6. Use the [trust curve](TRUST-CURVE.md) before scaling. Configure third-party tools separately using their current documentation.
