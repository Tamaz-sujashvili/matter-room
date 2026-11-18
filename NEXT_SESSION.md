# NEXT SESSION BRIEFING — read this first

You are picking up **Matter Room** for **Built with AutoClaw — Round 3**, Legal Practice track.

- Owner: Tamaz Sujashvili
- Deadline: **Friday 20 Nov 2026, 23:59 UTC+8 = 19:59 Tbilisi (UTC+4)**
- This folder is the repo. The demo matter is `examples/halden-safe/`.
- Do **not** redesign the architecture. The plan is `matter-room-plan.md`.

## Read order (do not skip)

1. This file
2. `matter-room-plan.md` — the execution plan (clock, deliverables, fallbacks)
3. `SKILL.md` — what AutoClaw reads and runs
4. `examples/halden-safe/raw/` — the Halden corpus (already drafted)
5. `prompts/` — council seats; do not improvise new seats

## What is already done vs what you must do

Done in this scaffold:

- Repo tree, plan, skill, prompts, templates, lint script, install script
- Halden raw corpus: SAFE, side letter, term sheet, 4 emails, cap table
- Contested facts are planted (pro rata, information rights timing, MFN scope, entire-agreement fight)

Not done (this is the work):

- Stamp `sha256` on every `raw/*.md` frontmatter (ingest step)
- Compile L2 wiki pages (entities, concepts, comparisons)
- Risk-rank top 5, run the four-reviewer council inside AutoClaw
- Produce the five deliverables in `examples/halden-safe/deliverables/`
- Run `scripts/lint_matter.py`, fix links, screenshot
- Hand-verify 8 claims into `verification_log.md` (include at least one `corrected`)
- Public GitHub push, X thread, form

## Clock (Tbilisi)

| Date | Phase |
|---|---|
| Wed 18 Nov | Ingest + compile + rehearsal. Council if time. |
| Thu 19 Nov | Full council, all deliverables, lint, verification log, push public |
| Fri 20 Nov | Record, post, submit form. **No new features.** |

## First command

```bash
cd /Users/tazo/Desktop/matter-room
python3 scripts/lint_matter.py examples/halden-safe
# then follow SKILL.md § Ingest on examples/halden-safe
```

## Hard rules for this entry

- AutoClaw Legal Assistant is the runtime. Do not boot Karpathy's Node council app.
- Do not redline the YC SAFE. Redline the side letter only.
- Every memo claim needs `[[raw/<file>.md#anchor]]`.
- Fictional matter. Do not swap in a real client document on Friday.
- One Legal entry. Second track only after the X post is live.
