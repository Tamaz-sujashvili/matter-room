---
title: Conversion and cap math
created: 2026-11-18
updated: 2026-11-18
type: concept
tags: [safe, cap-table, risk-medium, obligation]
risk: medium
contested: false
confidence: high
sources:
  - "[[raw/safe.md#1-definitions]]"
  - "[[raw/safe.md#2-purchase-conversion]]"
  - "[[raw/cap-table.md#post-money-math]]"
  - "[[raw/cap-table.md#option-pool]]"
---

# Conversion and cap math

The Safe converts at the lower of the financing price or the Safe Price, and the
Safe Price is the cap divided by Company Capitalization —
[[raw/safe.md#2-purchase-conversion]].

## The formula, in the instrument's own terms

- Company Capitalization = shares outstanding + converting securities + options
  and warrants + the **Unissued Option Pool**, but **excluding** this Safe, other
  Safes, and convertible notes — [[raw/safe.md#1-definitions]].
- Safe Price = Post-Money Valuation Cap ÷ Company Capitalization —
  [[raw/safe.md#1-definitions]].
- Here: $8,000,000 ÷ 10,000,000 shares = **$0.80 per share**.
- $400,000 ÷ $0.80 = **500,000 shares** — [[raw/cap-table.md#post-money-math]].

## The number that surprises founders

500,000 ÷ (10,000,000 + 500,000) = **4.7619%**, not 5.00% —
[[raw/cap-table.md#post-money-math]].

The 5.00% figure is Purchase Amount ÷ Cap. It describes the stake measured against
the pre-conversion base that the Safe itself is excluded from. Once the Safe's own
shares join the count, the stake is 4.76%. The gap is not a drafting error; it is
what the defined arithmetic produces, and the cap table states it plainly.

The option pool sits inside Company Capitalization, so the pool dilutes the
Investor at conversion and no top-up is modelled. The pool is 20.0% of
pre-conversion shares and 19.05% of post-conversion shares —
[[raw/cap-table.md#option-pool]].

## What is not modelled

- A real financing price. If the Series Seed prices above $0.80, the Safe Price
  controls and the Investor gets 500,000 shares. Below $0.80, the financing price
  controls and the cap never bites — [[raw/safe.md#2-purchase-conversion]].
- Any other Safe or note. None outstanding — [[raw/cap-table.md#post-money-math]].
- The side letter's pro rata right, which is not a conversion mechanic —
  [[raw/side-letter.md#2-pro-rata-rights]].

## Assessment

This clause is market-standard and correct. It is on the list because a founder
who plans dilution off the 5.00% headline will be 0.24 points wrong, and because
the pool is the lever she can still move before close. Issue-spot it; do not
redline a YC form over it — [[what-does-the-founder-owe]].

## Related

[[halden-analytics]] holds the shares. [[risk-rank-top-5]] places this fifth.
