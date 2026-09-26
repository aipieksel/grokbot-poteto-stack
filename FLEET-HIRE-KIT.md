# Fleet hire kit

Standing up a small Grok Bot fleet: **one global hire-then-train skill** + **public bot templates** for standing roles. Not a skill per role.

Requires: [GrokBot Poteto Stack](SKILL.md) operator skill (or the package `SKILL.md`) and a seeded `$OS` per project. See package `USAGE.md` for install vs share path.

Placeholders: `$WORKSPACE` = project root; `$OS` = `$WORKSPACE/operating-system`. Never hard-code one machine’s Shared folder as runtime `$OS`.

## Skill card vs public bot template

| Kind | What it is | When |
|------|------------|------|
| **Skill card** | Global recipe. No identity, no computer, no channel seat. | Process any bot can run (operator loop, approval gates, hire-then-train). |
| **Public bot template** | Shareable agent profile. Importer may rename. | Standing colleague with one job. |
| **Local only** | Private to one operator | Publishers, private SEO connectors, private monitors. Do not ship as public defaults. |

## Minimum public team

1. Operator skill (Poteto Stack)
2. Chief of Staff / Coordinator — one front door; designs/routes; does not produce
3. Researcher — sourced findings; no strategy/post
4. Docs — tag to append group runbook/skill

Add when needed: Designer, Proofreader, Dev Reviewer + Dev Coder.

Do not publish as public defaults: Publisher, SEO bots bound to private connectors, Life admin / Monitor / Speaking.

## Rename rules

1. Rename to taste after hire if you want a different name.
2. Sibling pointers use role titles or the names you chose.
3. Channels by domain; create only when 2+ bots share a domain.
4. One chief per fleet.

## Hire-then-train

1. Install Poteto Stack skill once account-wide.
2. Seed `$OS` per project on the machine that runs the work. Share/pack path is not runtime `$OS`.
3. Hire minimum bots from public templates.
4. Rename and seat in rooms.
5. Trust curve: one agent, watch everything, encode failures as skills, eval, then routines / cloud parallel.
6. First E2E packet through Researcher before any automation.
7. Stop before publish, send, spend, or delete without human approval.

## Must not

- A skill per role that only says be helpful
- Publishing logged-in Publisher or private SEO bots as public templates
- Two chiefs of staff
- Hard-coding a Shared path as runtime `$OS`
- Secrets or private URLs in public skills or templates
