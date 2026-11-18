# Matter Room SCHEMA — Halden / Meridian

Conventions for this constructed financing matter. Read before ingest, council, or lint.

## Domain

Pre-close review of a YC Post-Money Safe plus a draft side letter plus four emails plus a term sheet plus a cap table. Live question: what does the founder actually owe, and what gets redlined in the side letter before Monday 23 Nov 2026?

This matter is **fictional**. Do not replace names with real ones.

## Layers

- **L1 `raw/`** — immutable sources. SHA256 in frontmatter. Never edit the body after first ingest.
- **L2** `entities/` `concepts/` `comparisons/` `queries/` — agent-owned pages.
- **`deliverables/`** — memo, redline, timeline, evidence index, verification log.

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

## Tag Taxonomy

- party: party, person
- instrument: safe, side-letter, term-sheet, email, cap-table
- risk: risk-high, risk-medium, risk-low, closing-critical, date-critical
- state: contested, uncited, obligation, right

## Page thresholds

Create a page for: a party, a person, an instrument, a contested fact, a high-risk clause, a comparison. Do not create a page for a passing defined term.

Every L2 page: ≥2 outbound `[[wikilinks]]`.

## Planted tensions (the council must find these — do not pre-solve them in L2 before the council runs)

1. **Pro rata** — term sheet: until Series Seed; email-02: “of course going forward”; side letter: until Equity Financing; SAFE: silent / no grant.
2. **Information rights** — term sheet: at Series Seed; email-03: founder says not now; email-04 / side letter: monthly from day one; SAFE §4: no stockholder or information rights.
3. **MFN scope** — term sheet: subsequent Safes only; email-04 / side letter: Safes **or convertible notes**.
4. **Entire agreement** — SAFE §6.2 vs side letter §5.2 (“this Side Letter shall control”) and §1.2 (“amend and complement”).
5. **Pro Rata Share definition** — side letter §2.2 is circular (“maintain its percentage ownership as of the date of this Side Letter”) and the exercise period is “as reasonably agreed.”
6. **Cap math** — 5.00% of the cap vs ~4.76% of then-outstanding; option pool included in Company Capitalization.

## Update policy

On conflict: write both claims, `contested: true`, two sources. Do not silently pick a winner. Emails are evidence of intent, not executed amendments.

## What this matter is not

Not a research wiki. Deliverables address the live question only.
