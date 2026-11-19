# Matter Room SCHEMA

Conventions for this matter. Read this before ingest, query, or lint.

## Domain

Legal matter file: contracts, side letters, term sheets, emails, cap table.
Constructed financing matter unless the human says otherwise.

## Layers

- **L1 `raw/`** — immutable sources. SHA256 in frontmatter. Never edit the body.
- **L2** `entities/` `concepts/` `comparisons/` `queries/` — agent-owned pages.
- **`deliverables/`** — closing brief (first on a pre-close review), memo, redline,
  timeline, evidence index, verification log.

## Citation rule

Every factual claim carries `[[raw/<file>.md#<anchor>]]`.
No locator → `confidence: low` → may not enter the memo.

## Frontmatter (required on every L2 page)

```yaml
title:
created:
updated:
type: entity | concept | comparison | query | deliverable
tags:
risk: high | medium | low
contested: true | false
confidence: high | medium | low
sources:
  - "[[raw/...]]"
```

`contested: true` → at least two sources.
`risk: high` → at least one `[[raw/...]]` in the body.

## Evidence labels (brief and memo)

`**signed term**` · `**express agreement**` · `**proposal**` · `**unresolved**`

One label per agreement claim, inline, with the quotation beside it. Draft
language and "we'll consider" are `proposal`. Silence and unanswered questions are
`unresolved`. An unsigned instrument binds nobody.

## Tag Taxonomy

- party: party, person
- instrument: safe, side-letter, term-sheet, email, cap-table
- risk: risk-high, risk-medium, risk-low, closing-critical, date-critical
- state: contested, uncited, obligation, right

## Page thresholds

Create a page for: a party, a person, an instrument, a contested fact, a
high-risk clause, a comparison. Do not create a page for a passing defined term.

Every L2 page: ≥2 outbound `[[wikilinks]]`.

## Update policy

On conflict between sources: write both claims, `contested: true`, two sources,
flag for the council's Consistency seat. Do not silently pick a winner.

## What this matter is not

Not a research wiki. Not a blog. Not a place to store legal advice to the world.
Deliverables address the live question of this matter only.
