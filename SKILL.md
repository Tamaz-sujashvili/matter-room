---
name: matter-room
description: >-
  Turn a contract bundle into a matter file: a one-page closing brief, evidence
  wiki, fact timeline, evidence index, multi-reviewer council memo, and a
  side-letter redline. Use when the user asks what binds before a signature, to
  review a contract before close, compare documents, organize a matter file,
  draft a redline, or run a legal council in AutoClaw Legal Assistant.
  Reverse-engineered from create-wiki + llm-council-skill.
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

## Pre-close review → the closing brief is the first result

If the ask is a pre-close review — a signature is pending, a wire date is set, or
the user asks *what binds today* or *what should I push* — the first deliverable,
and the first link under Deliverables in `index.md`, is
`deliverables/closing_brief.md`.

Nothing else is written until it exists: no memo, no council, no timeline. Ingest
still runs first, because the brief cites it.

### Cap: 350 reader-facing words

Reader-facing means what a partner reads: headings, prose, table cells, link
labels. Frontmatter, HTML comments and `[[path#anchor]]` targets do not count.
`scripts/lint_matter.py` counts the file and fails above 350. Do not evade the cap
by moving text into a table, a comment, or a collapsed section — the reader still
reads it, so the counter still counts it.

### Three sections, in this order, always

1. **What binds today** — executed instruments, and the carve-outs a non-binding
   term sheet keeps binding. Nothing unsigned.
2. **Three edits to push before signing** — exactly three, ranked. Each names the
   clause, the source, and the change number in `deliverables/redline.md`.
3. **What counsel still needs to confirm** — open facts and open asks. No advice,
   no invented answer.

A brief that lists five edits is a memo with a shorter title. Three is the
decision the partner has to make on the call.

### Evidence labels — at the point of use

Every statement about what another party has agreed to carries one label, inline,
next to the claim. Never in a legend the reader has to look up.

| Label | Means | Test that must pass |
|---|---|---|
| **signed term** | Executed instrument in `raw/` | A signature page and a stamped hash |
| **express agreement** | Unambiguous written commitment | Quote the sentence; it must say the thing |
| **proposal** | Offered, not accepted | Draft language, "we'll consider", "happy to" |
| **unresolved** | Nothing in the bundle decides it | Absence, a question with no reply, silence |

Hard rules:

- **Quote before you claim.** The quotation and its `[[raw/...#anchor]]` sit in the
  same sentence as the label. A claim of agreement with no quotation is
  `unresolved`, whatever the email's tone suggests.
- **Draft language is a proposal**, even when drafted as an obligation ("the
  Company shall deliver"). The side letter is a draft until it is signed.
- **Silence stays unresolved.** One side asked, the other never replied: that is
  `unresolved`, written as "no reply in the bundle" — not consent, not waiver.
- **Read the term sheet's binding carve-outs before concluding what binds.** A
  non-binding term sheet normally keeps confidentiality and expenses binding.
  Name those provisions, then say what the rest of it does and does not do.
- **Label, then recommend.** You may recommend pushing for a `proposal`. Say that
  it is one. Do not upgrade a label to make the recommendation read cleaner.
- **An unsigned letter changes nothing about today.** State what binds now, and
  state separately what will bind on signature.

### The redline link

Every recommendation points at one numbered change in `deliverables/redline.md`,
and that change carries the Before and After text. A recommendation with no
redline change is an opinion.

A change heading **is** the anchor, so keep it short and slug-friendly:
`## Change 1 — precedence` cites as `[[deliverables/redline#change-1-precedence]]`.
Put the clause number in the body, not in the heading, or the anchor acquires a
`52` in the middle of it and stops matching. The linter checks anchors into
`deliverables/` and `council/` as well as `raw/`.

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
└── deliverables/       # closing brief, memo, redline, timeline, evidence index, verification log
```

- **L1 raw/** is immutable after ingest. Corrections live in L2 pages.
- **L2 pages** are agent-owned markdown with frontmatter and `[[wikilinks]]`.
- **deliverables/** are the only files that leave the matter.

## Citation rule (non-negotiable)

Every factual claim in an L2 page or deliverable carries a locator:

```
[[raw/safe.md#6-miscellaneous]]          # §6.2 lives in §6
[[raw/email-04.md#email-04-16-nov-2026]] # the date is in the heading
[[raw/cap-table.md#post-money-math]]
```

**Anchors are heading slugs, not section numbers.** Lowercase the heading text,
drop punctuation, turn spaces into hyphens: `## 2. Purchase; Conversion` becomes
`#2-purchase-conversion`. A clause with no heading of its own is cited to the
nearest heading, with the clause number in the prose ("§6.2"). The linter fails a
citation whose anchor does not exist, so a wrong slug is caught, not published.

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
  - "[[raw/safe.md#6-miscellaneous]]"
  - "[[raw/side-letter.md#4-most-favored-nation]]"
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

Order depends on the ask. A pre-close review runs **1 → the closing brief → stop**,
and only continues into risk rank, council and memo if the user asks for them. A
full matter review runs 1 → 2 → 3 → 4 → 5 → 6.

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

#### Anchors that exist in a financing matter

Anchors are the headings the source actually has. Check before you cite; the
linter rejects anything else.

| Source | Anchors |
|---|---|
| SAFE | `#1-definitions` `#2-purchase-conversion` `#3-subsequent-issuances-this-instrument-is-silent` `#4-no-stockholder-rights` `#6-miscellaneous` `#signature-page` |
| Side letter | `#1-recitals` `#2-pro-rata-rights` `#3-information-rights` `#4-most-favored-nation` `#5-conflict-entire-agreement` `#6-miscellaneous` |
| Term sheet | `#investment` (the row table — name the row in prose) `#other` |
| Emails | `#email-01-12-nov-2026` … `#email-04-16-nov-2026` |
| Cap table | `#outstanding` `#post-money-math` `#option-pool` `#what-this-table-does-not-model` |

If a row or clause deserves its own anchor, give the source a heading — do that
**before** ingest. After ingest the body is frozen and the nearest heading is the
best locator available.

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

Four legal checks on top of the wiki checks (broken links, orphans, index
completeness, frontmatter, SHA drift, page size), plus five on the closing brief:

1. **uncited-high-risk** — `risk: high` with no `[[raw/...]]` in the body
2. **contested-unpaired** — `contested: true` with fewer than two sources
3. **deliverable-backlink** — a file in `deliverables/` missing from `index.md`
4. **bad-anchor** — `[[raw/x.md#anchor]]`, `[[deliverables/y.md#anchor]]` or
   `[[council/z.md#anchor]]` where the heading does not exist
5. **brief-length** — more than 350 reader-facing words
6. **brief-structure** — one of the three fixed sections is missing
7. **brief-count** — the declared count (`<!-- reader-facing words: N -->`) no
   longer matches the file
8. **brief-redline** — no recommendation links to a numbered change in
   `deliverables/redline.md`
9. **brief-unlabelled** — no evidence label anywhere in the brief

Then manually verify what the script cannot judge (contradictions, stale law,
whether a quotation actually supports the claim built on it).

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
| `deliverables/closing_brief.md` | First result of a pre-close review. ≤ 350 reader-facing words, three sections in the fixed order, every agreement claim labelled and quoted, each recommendation linked to one redline change. `lint_matter.py` enforces the cap, the section set and the declared count. |
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
- **Do not state that a party agreed without quoting the sentence** — quote first,
  label second, recommend third
- **Do not treat silence, a draft, or "we'll consider" as agreement** — proposal
  and unresolved are the honest labels and the ones that survive a partner's read
- **Do not put client-identifying data in a public post** — if the matter is
  real, redact before any screenshot; if constructed, say so
- **Keep pages under 200 lines**
- **Handle contradictions explicitly** — both claims, `contested: true`, two sources

## Additional resources

- Plan: `matter-room-plan.md`
- Example matter: `examples/halden-safe/`
- Council prompts: `prompts/`
- Lint: `scripts/lint_matter.py`
