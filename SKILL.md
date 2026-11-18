---
name: matter-room
description: >-
  Turn a contract bundle into a matter file: evidence wiki, fact timeline,
  evidence index, multi-reviewer council memo, and a side-letter redline.
  Use when the user asks to review a contract, compare documents, organize a
  matter file, draft a redline, or run a legal council in AutoClaw Legal
  Assistant. Reverse-engineered from create-wiki + llm-council-skill.
---

# Matter Room Skill

Run a legal matter from a folder of sources to five checked deliverables,
entirely inside this agent. Based on Karpathy's LLM Wiki pattern (librarian,
not chatbot) and Karpathy's LLM Council protocol (parallel opinions →
anonymized peer review → chairman). No second model stack. No Node app.

**Division of labor:** The human owns the matter, the verification log, and
every platform post. The agent ingests, compiles, councils, drafts, and lints.
The agent never marks a claim `verified`.

## When to use

- "Review this SAFE / MSA / NDA / side letter"
- "Compare template vs executed"
- "Organize these emails and contracts into a matter file"
- "Run Matter Room on this folder"
- "Redline the side letter before close"

## Matter location

Resolve the matter root at session start:

```bash
MATTER="${MATTER_PATH:-$PWD}"
```

If the folder has no `SCHEMA.md`, initialize it from `templates/` first.

## Architecture

```
matter/
├── SCHEMA.md           # conventions, tag taxonomy, citation rule
├── index.md            # catalog
├── log.md              # append-only action log
├── raw/                # L1: immutable sources (SHA256)
│   ├── safe.md
│   ├── side-letter.md
│   ├── term-sheet.md
│   ├── email-01..04.md
│   └── cap-table.md
├── entities/           # L2: parties, people, instruments-as-parties
├── concepts/           # L2: obligations, rights, risks
├── comparisons/        # L2: template vs executed, SAFE vs side letter
├── queries/            # L2: filed questions
└── deliverables/       # memo, redline, timeline, evidence index, verification log
```

- **L1 raw/** is immutable after ingest. Corrections live in L2 pages.
- **L2 pages** are agent-owned markdown with frontmatter and `[[wikilinks]]`.
- **deliverables/** are the only files that leave the matter.

## Citation rule (non-negotiable)

Every factual claim in an L2 page or deliverable carries a locator:

```
[[raw/safe.md#s7-entire-agreement]]
[[raw/email-04.md#2026-11-16]]
[[raw/cap-table.md#post-money-math]]
```

A claim without a locator is `confidence: low` and **may not enter the memo**.

## Frontmatter (every L2 page)

```yaml
---
title: ...
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | deliverable
tags: [obligation, risk-high, contested]
risk: high | medium | low
contested: true | false
confidence: high | medium | low
sources:
  - "[[raw/safe.md#s7-entire-agreement]]"
  - "[[raw/side-letter.md#s4-mfn]]"
---
```

`contested: true` requires **at least two** `sources`. `risk: high` requires at
least one `[[raw/...]]` citation in the body.

## Tag taxonomy (closed list — add to SCHEMA.md before inventing)

`obligation`, `right`, `risk-high`, `risk-medium`, `risk-low`, `contested`,
`uncited`, `safe`, `side-letter`, `term-sheet`, `email`, `cap-table`,
`closing-critical`, `party`, `person`, `date-critical`

## Resuming a matter (CRITICAL)

Before ingest, council, or lint:

1. Read `SCHEMA.md`
2. Read `index.md`
3. Read the last 20–30 lines of `log.md`

Only then proceed. This prevents duplicate pages and missed cross-references.

## Initializing a new matter

1. Resolve path
2. Copy `templates/` into the matter root (keep `raw/` empty)
3. Ask what the matter is, or detect from filenames
4. Write `SCHEMA.md` customized to the domain (SAFE vs MSA vs employment)
5. Write `index.md` and `log.md` with a creation entry
6. Confirm ready and list the first sources to ingest

## Core operations

### 1. Ingest

For each file the user drops into `raw/` (or names):

**① Stamp the source**

- Compute SHA256 of the body below frontmatter
- Write `sha256`, `source_url` (if any), `ingested` date into raw frontmatter
- On re-ingest: recompute SHA256 — skip if identical, flag drift if changed
- Never edit the body of a raw file after first ingest

**② Check what exists** — read `index.md`, search entities/concepts

**③ Write or update L2 pages**

- New pages only if they meet page thresholds (party, instrument, contested
  fact, high-risk clause, or comparison — not a passing defined term)
- Every page links to ≥2 other pages
- Tags only from the taxonomy
- Provenance: `[[raw/<file>.md#anchor]]` on every claim
- `confidence: medium|low` for single-source or inferred claims

**④ Update `index.md` and append `log.md`**

**⑤ Report files touched**

A single source often updates 5–10 pages. That compounding is intentional.

#### Suggested anchors for a financing matter

| Source | Anchors |
|---|---|
| SAFE | `#s1-definitions` `#s2-conversion` `#s3-dissolution` `#s4-liquidity` `#s5-no-stockholder-rights` `#s7-entire-agreement` |
| Side letter | `#s1-recitals` `#s2-pro-rata` `#s3-information` `#s4-mfn` `#s5-conflict` `#s6-misc` |
| Term sheet | `#row-pro-rata` `#row-info-rights` `#row-mfn` `#row-cap` `#row-close` |
| Emails | `#YYYY-MM-DD` |
| Cap table | `#post-money-math` `#option-pool` |

### 2. Risk rank (before council)

Run `prompts/risk_rank.md` against `index.md` + all L2 pages.

Output a ranked top-5. Weight: **money → control → exit → missing → ambiguity**.

Silence can rank (a missing standard term). Do not invent terms to fill gaps.

### 3. Council (inside this agent — no second app)

Four seats, same five clauses, one turn each. Reviewers see the clause, the
cited raw text, and nothing about the other seats.

| Seat | Prompt | Looks for |
|---|---|---|
| A — Risk | `prompts/reviewer_risk.md` | Dilution, cap math, dissolution, uncapped exposure |
| B — Missing | `prompts/reviewer_missing.md` | Standard terms omitted (pro rata mechanics, notice, amendment) |
| C — Consistency | `prompts/reviewer_consistency.md` | Side letter vs SAFE entire-agreement; emails vs paper |
| D — Ambiguity | `prompts/reviewer_ambiguity.md` | Undefined terms, conversion mechanics, which document wins |

**Stage 2 — anonymized review.** Collect the four outputs. Strip seat names.
Label them Response A/B/C/D. One extra turn: rank each on accuracy and insight.
Last line must be `FINAL RANKING:`.

**Stage 3 — Chairman.** `prompts/chairman.md`. Reads stage-1 outputs + rankings.
Writes the memo. **Keeps disagreements.** A council that always agrees is one
model with extra steps.

If context is tight, council **one clause per turn**. Never drop the chairman.

### 4. Redline (side letter or other negotiated doc — not the market-standard form)

Use `templates/redline.md`:

- `~~struck~~` **inserted**
- Each change has a footnote: which reviewer, which `[[source]]`
- No silent rewrites
- Do not redline a YC SAFE, NVCA model doc, or other market standard — issue-spot
  it in the memo instead

### 5. Timeline + evidence index

- `deliverables/fact_timeline.md` — dated rows, each cited, contested dates marked
- `deliverables/evidence_index.md` — one row per raw file: path, SHA256, what it
  supports, what it contradicts

### 6. Lint

```bash
python3 scripts/lint_matter.py "$MATTER"
# or --json for agent parsing
```

Then manually verify what the script cannot judge (contradictions, stale law).

Append to `log.md`: `## [YYYY-MM-DD] lint | N issues found`

The lint screenshot is the "sources were checked" artifact. Fix broken links
and orphans before any post.

### 7. Verify (human-owned)

The agent proposes eight claims in `deliverables/verification_log.md` with
locators and quoted source text, all rows `pending`.

The human marks each `verified` / `corrected` / `could not verify`.

If `corrected`: fix the memo **and** the L2 page **and** the log. Leave the
correction visible.

The agent never fills in `verified` by itself.

## Deliverables — definition of done

| File | Done when |
|---|---|
| `deliverables/research_memo.md` | Issue → what the documents say (cited) → assessment → recommended action. Opens with the live question. ≤ 4 pages. Council disagreements appear. |
| `deliverables/redline.md` | Negotiated doc only. Every change footnoted. |
| `deliverables/fact_timeline.md` | Dated rows, each cited. Contested dates marked. |
| `deliverables/evidence_index.md` | One row per raw file, SHA256 filled. |
| `deliverables/verification_log.md` | Eight claims, quoted sources, human verdicts. At least one `corrected` is normal. |

## Pitfalls

- **Never modify `raw/` after ingest**
- **Always orient first** — SCHEMA + index + recent log
- **Always update index.md and log.md**
- **Do not redline a market-standard form**
- **Do not run a second LLM app for the council**
- **Do not mark a claim verified**
- **Do not put client-identifying data in a public post** — if the matter is
  real, redact before any screenshot; if constructed, say so
- **Keep pages under 200 lines**
- **Handle contradictions explicitly** — both claims, `contested: true`, two sources

## Additional resources

- Plan: `matter-room-plan.md`
- Example matter: `examples/halden-safe/`
- Council prompts: `prompts/`
- Lint: `scripts/lint_matter.py`
