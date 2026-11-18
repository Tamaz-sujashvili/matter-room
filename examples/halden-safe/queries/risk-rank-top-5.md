---
title: Risk rank — top five before the council
created: 2026-11-18
updated: 2026-11-18
type: query
tags: [risk-high, closing-critical, safe, side-letter]
risk: high
contested: false
confidence: high
sources:
  - "[[raw/side-letter.md#4-most-favored-nation]]"
  - "[[raw/side-letter.md#3-information-rights]]"
  - "[[raw/side-letter.md#2-pro-rata-rights]]"
  - "[[raw/side-letter.md#5-conflict-entire-agreement]]"
  - "[[raw/safe.md#1-definitions]]"
---

# Risk rank — top five before the council

Produced by `prompts/risk_rank.md` over `index.md` and every L2 page, before any
council turn. Weight: **money → control → exit → missing → ambiguity**. Silence
counts: a clause that is absent can rank.

| # | Clause | Weight | Why it is here |
|---|---|---|---|
| 1 | **MFN §4.1–4.2** — reaches convertible notes; "more favorable" includes "additional rights" | Money | An MFN over a bridge note resets the cap to whatever the bridge says. Uncapped, automatic, no notice — [[raw/side-letter.md#4-most-favored-nation]] |
| 2 | **Information rights §3.1–3.2** — monthly within 15 days, budget, on-request, inspection | Control | A recurring covenant at pre-seed with no end date and no confidentiality clause — [[raw/side-letter.md#3-information-rights]] |
| 3 | **Pro rata §2.1–2.3** — reaches any issuance of Capital Stock; circular share; no price; "as reasonably agreed" | Control | Dilution protection over a class of issuances the term sheet never covered, whose size cannot be computed — [[raw/side-letter.md#2-pro-rata-rights]] |
| 4 | **Conflict clause §5.2** vs Safe §6.2 | Structural | Decides which document wins; amplifies 1–3 rather than adding exposure of its own — [[raw/side-letter.md#5-conflict-entire-agreement]] |
| 5 | **Cap math and option pool** — 5.00% headline, 4.76% issued, pool inside Company Capitalization | Money | Market-standard and correct, but the founder's dilution model is 0.24 points off — [[raw/safe.md#1-definitions]] |

## Why §5.2 is fourth, not first

The memo opens with the entire-agreement fight because that is the question the
client asked. On **exposure**, §5.2 ranks fourth: remove it and the letter still
grants the same three rights, so its own damage is derivative. It multiplies
clauses 1–3 rather than creating anything new — and it is the cheapest of the five
to delete, which is why it belongs in the redline set even at fourth place.

## Why the missing terms do not get their own row

Four absences matter and each is folded into the clause it damages:

- no notice period before an MFN trigger — folded into 1
- no sunset on reporting, and a §6.4 exception that refers to nothing — folded into 2
- no fixed exercise window for pro rata, and no stated price — folded into 3
- no clause saying how the letter itself is amended — mentioned in
  [[safe-vs-side-letter]], not ranked; low value at this size

## Not ranked

- **Board seat.** Term sheet says none and the letter does not ask —
  [[raw/term-sheet.md#investment]].
- **The 20 November signature ask.** A scheduling demand, not a clause —
  [[raw/email-04.md#email-04-16-nov-2026]].
- **The 5.00% vs 4.76% gap as a *drafting* defect.** It is not one. The arithmetic
  is what the definitions produce — [[conversion-and-cap-math]].

## Handoff

These five clauses, and only these five, go to the four reviewer seats. See
`council/01-risk.md` through `council/04-ambiguity.md`. Conclusion:
[[what-does-the-founder-owe]].
