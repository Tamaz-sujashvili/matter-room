# Seat C — Consistency

Prompt: `prompts/reviewer_consistency.md`. Ran 18 Nov 2026, one turn, packet only.

## Ranking by exposure to the Company

1. Conflict clause §5.2 against Safe §6.2 — this decides whether anything else in
   this list survives
2. MFN §4.1 — grants more than any document that came before it
3. Information rights §3.1 — grants the opposite of what the Company said it would
   accept, one day after saying it
4. Pro rata §2.1 — duration drifts from the term sheet
5. Cap math — consistent throughout

## 1. The Safe supersedes the side letter

Safe §6.2 supersedes "all prior agreements, understandings, term sheets, and
negotiations, whether written or oral" — [[raw/safe.md#6-miscellaneous]].

The side letter is not a fresh grant. It is the papering of something expressly
under discussion before the Safe was signed: counsel's 12 November email refers to
"the lead-investor points we discussed on the 6 November call" —
[[raw/email-01.md#email-01-12-nov-2026]]. A term agreed on 6 November and papered
on 16 November is a prior understanding within §6.2. Signing it does not cure
that; §6.2 already extinguished it.

The side letter's answer to this is §5.2 — "this Side Letter shall control" —
[[raw/side-letter.md#5-conflict-entire-agreement]]. A clause in the later document
cannot revive a right the earlier document destroyed, and §5.2 is in the document
whose validity is in question. It is bootstrapping.

**Note the tension the drafter has to live with:** §1.2 says the letter "amends
and complements" the Safe — [[raw/side-letter.md#1-recitals]] — while §5.1 says the
two documents together are the entire agreement —
[[raw/side-letter.md#5-conflict-entire-agreement]]. If the letter amends the Safe,
the Safe is no longer the whole agreement and §5.1 is wrong. If both together are
the whole agreement, nothing was amended. It cannot be both.

## 2. MFN — every layer adds scope

| Layer | Date | Scope | Cite |
|---|---|---|---|
| Term sheet | 28 Oct | Subsequent **Safes** | [[raw/term-sheet.md#investment]] |
| 6 Nov call | 6 Nov | Not documented anywhere in the bundle | — |
| Email 02 | 13 Nov | Does not mention MFN | [[raw/email-02.md#email-02-13-nov-2026]] |
| Email 03 | 14 Nov | Asks whether notes are included | [[raw/email-03.md#email-03-14-nov-2026]] |
| Email 04 | 16 Nov | "Safe **or convertible promissory note**" | [[raw/email-04.md#email-04-16-nov-2026]] |
| Side letter | 16 Nov | Safes or notes, plus "additional rights" | [[raw/side-letter.md#4-most-favored-nation]] |

Counsel justifies the widening by the 6 November call —
[[raw/email-04.md#email-04-16-nov-2026]]. That call is precisely what §6.2
supersedes, and there is no written record of it in the bundle. An oral prior
negotiation cannot support a term in a document that disclaims all prior oral
negotiations.

## 3. Information rights — the Company said one thing, the letter says another

14 November: "I don't want a contractual reporting covenant at pre-seed" —
[[raw/email-03.md#email-03-14-nov-2026]]. 16 November: monthly financials within
15 days — [[raw/side-letter.md#3-information-rights]]. No reply from the Company in
the bundle. Silence is not consent, but it is also not a record of objection, and
the letter is drafted as if the point were settled.

## 4. Pro rata — two different end dates

Term sheet: "until Series Seed" — [[raw/term-sheet.md#investment]]. Letter: "until
the closing of an Equity Financing" — [[raw/side-letter.md#2-pro-rata-rights]].
"Equity Financing" is defined in the Safe without reference to a series
designation — [[raw/safe.md#1-definitions]]. A bridge priced as a priced equity
round would close the right early; a Series Seed Preferred would close it as
expected. The documents do not agree on which.

## 5. Cap math — no inconsistency

Term sheet $8M cap and no discount — [[raw/term-sheet.md#investment]]; Safe $8M cap
and no discount — [[raw/safe.md#1-definitions]]; cap table arithmetic —
[[raw/cap-table.md#post-money-math]]. All three agree.

## What I would change first

Do not sign §5.2 as drafted. Either the letter is effective as a signed amendment
under §6.3, in which case §5.2 is unnecessary, or it is not, in which case §5.2
does not save it. Delete §5.2, keep §1.2, and state in one line that the letter
amends the Safe only as expressly provided in it.
