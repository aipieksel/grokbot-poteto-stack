---
name: grokbot-poteto-stack
description: Use when Grok Bot should own the workflow as operator, run a coordinator + specialist fleet (default Scout), keep shared $OS context, enforce approval gates, and follow the Lauren trust curve for Cursor pstack coding. Kimi optional only.
---

# GrokBot Poteto Stack

Reusable operating pattern: **Grok Bot runs the work. A named fleet specialist returns intelligence.** The operator (or your coordinator) owns the workflow and final action. Specialist default: **Scout**. Kimi is **not required**.

Sources to credit when quoting claims:

- Lauren Tan (@poteto) trust curve / pstack / Grok Bot team (workshop + MTS demo + pstack docs). See `docs/TRUST-CURVE.md` and `docs/GROK-BOT-TEAM.md` in this package.
- Alex (@de1lymoon) Grok + specialist OS pattern is optional background only. Not an xAI/Cursor product tutorial.

Placeholders: `$WORKSPACE` = your project root; `$OS` = `$WORKSPACE/operating-system` (seed with `scripts/seed-os.sh`).

---

## 1. Lauren trust curve (do this before you scale)

Treat agents like reports you do not trust yet. Do not jump to many cloud agents from low trust.

1. **Start local, one agent, watch everything.** Stay in the loop. Open tool calls, thinking, screenshots. You are the verifier.
2. **Install pstack (Cursor)** when coding work needs rigor:
   - `/add-plugin pstack`
   - `/setup-pstack` (maps models; writes `~/.cursor/rules/pstack-models.mdc`)
   - Open a **new chat** so the rule loads
   - `/poteto-mode <goal>. Done means <checkable evidence>.`
3. **Build a verification skill for your app** before you parallelize. Green build is not enough; the agent must drive the real product. pstack helpers (author claim / docs): `/create-verification-skill`, `/maintain-verification-skill`.
4. **Every failure becomes a markdown skill.** Encode where the agent guessed; force search, sub-agents, stop guessing.
5. **Eval skills before you trust them.** poteto-mode ships an eval playbook (author claim): rubric, isolated runs, cross-model judge, `/loop` until score is solid. Re-run after every skill change.
6. **Only then scale to cloud.** Same skills pay off on cloud agents once local verification is trusted. Auto-merge is a late Lauren claim after this ladder, not a setup step.

Cost caveat (Lauren): labs with unlimited tokens can overspend; do not copy spend blindly.

Full install order: `docs/GETTING-STARTED.md`. Coding adapter: `adapters/cursor-pstack.md`.

---

## 2. Grok as control plane (operator charter)

```
You are the operator.
Complete work yourself when the task is operational.
Delegate to a named specialist (default: Scout) when the task requires:
deep research, large-context analysis, source synthesis,
or complex technical reasoning.
The specialist returns intelligence.
You remain responsible for the final action.
Keep one coordinator for the fleet; do not invent a second chief of staff.
```

Operator loop (every request):

1. Understand the outcome
2. Inspect available context under `$OS`
3. Choose the shortest path
4. Call a specialist only when needed
5. Verify the result
6. Stop before irreversible actions

Prefer existing fleet bots (Scout, AEO, Dev, Docs, …) over inventing a new twin.

---

## 3. When to call a specialist vs do it yourself

**Operator does it** when the work is operational: file edits, browser steps, Slack/calendar/tool use, drafting from known context, running commands, applying a known playbook.

**Call Scout (or another named fleet bot)** when the bottleneck is thinking, not clicking:

- Deep research across many sources
- Long-context analysis
- Source synthesis
- Complex technical reasoning
- Parallelizable multi-entity research (swarm only when truly parallel; see §6)

**Do not** run two models on the same task and pick the nicer answer. Give ownership. Mark third-party Agent Swarm capacity numbers as **author claims** unless you verify them yourself.

Kimi is optional paid API only (see §10). Your fleet already covers the specialist slot.

---

## 4. Job packet shape

```
TASK: <one clear analysis or research job>
GOAL: <decision or artifact the packet must unlock>
RETURN:
- finding
- evidence
- source
- confidence
- recommended action
Do not execute anything.
```

Always include **Do not execute**. Specialists are intelligence-only in this pattern unless the human explicitly assigns execution to that bot's own computer under approval gates.

---

## 5. Shared context layer

```
$OS/
  context/   goals.md, projects.md, preferences.md, trusted-sources.md
  memory/    findings.json, decisions.json
  tasks/     active.json, completed.json
  agents/    operator.md, specialist.md
```

Flow:

1. Operator reads `$OS/context/*` and `$OS/tasks/active.json` (and recent memory) at start of work
2. Specialist gets **only** the packet plus the slices it needs
3. Write findings/decisions back to `$OS/memory/`
4. Update `$OS/tasks/` when work starts or finishes
5. Next run starts from disk, not from chat history

Prefer short, dated, evidence-backed notes. Prefer append + summarize over rewriting history away. **No secrets in `$OS`.**

---

## 6. Swarm only when parallelizable

Keep simple tasks simple. Use parallel / swarm-style research only when the job splits into many **independent** searches.

```
Research these items in parallel.
For each one find: <fixed fields>.
Verify major claims and return one normalized dataset.
Do not execute anything.
```

If steps depend on each other, keep one specialist thread.

---

## 7. Research → action handoff back to the operator

```
Turn this research into action.
Return:
1. what changed
2. why it matters
3. what we should do
4. what you can execute
5. what requires approval
```

Then the operator updates `$OS`, drafts follow-ups, executes reversible internal steps, and requests approval for gated steps.

---

## 8. Recurring loops (only after the manual path works)

```
Every <cadence>, inspect what changed since the last run.
Use a specialist when broad research is required.
Ignore repeated information.
Update memory with new findings.
Return only: important change, evidence, impact, next action.
```

Wire via Grok Bot routines / automations when available. Do not automate a path you have not verified manually.

---

## 9. Approval gates

Execute reversible internal actions autonomously (local notes, drafts, read-only research, updating `$OS` memory).

**Stop for approval before:**

- sending
- publishing
- spending
- deleting
- changing permissions
- making external commitments

End state: Grok / coordinator = workflow · Scout (or named bot) = deeper research · `$OS` = memory · automation = loops · human = judgment.

---

## 10. Kimi (optional paid API only)

Kimi is **not required**. Prefer Scout / existing specialists.

If you still want a paid Kimi API path later, follow `docs/OPTIONAL-KIMI.md`.

Until then: do not invent connectors, do not claim a native Grok↔Kimi product bridge, and do not store secrets in `$OS`.

---

## 11. Other surfaces

Same charter travels via thin adapters:

- `adapters/grok-bot.md`, `adapters/cursor-pstack.md` (primary)
- `adapters/codex.md`, `adapters/grok-cli.md`, `adapters/chatgpt.md` (secondary)
- `adapters/AGENTS.md.example`

---

## Quick checklist

- [ ] Trust curve: local one-agent verify → pstack → verification skill → failures→skills → eval → then cloud
- [ ] Operator charter loaded on Grok; one coordinator only
- [ ] Specialist = Scout (or named fleet bot); Kimi not required
- [ ] `$OS` tree present and readable/writable; no secrets inside
- [ ] Job packets use TASK / GOAL / RETURN + Do not execute
- [ ] Handoff back to operator for action + approval split
- [ ] Recurring loop only after one successful manual run
- [ ] Optional: `docs/OPTIONAL-KIMI.md` only if pursuing paid API
