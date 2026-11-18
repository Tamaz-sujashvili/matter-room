# Seat D — Ambiguity

Prompt: `prompts/reviewer_ambiguity.md`. Ran 18 Nov 2026, one turn, packet only.

## Ranking by exposure to the Company

1. Pro rata §2.2 — the definition does not compute
2. MFN §4.1–4.2 — "more favorable" is open-ended
3. Information rights §6.4 — survival clause refers to nothing
4. Conflict clause §5.1–5.2 — two clauses answer one question differently
5. Cap math — no ambiguity found

## 1. Pro Rata Share is circular

§2.2: "the fraction the Investor would need to maintain its percentage ownership of
the Company **as of the date of this Side Letter**" —
[[raw/side-letter.md#2-pro-rata-rights]].

On 16 November the Investor owns no shares. The Safe has not converted; §4 of the
Safe says it has no stockholder rights until it does —
[[raw/safe.md#4-no-stockholder-rights]]. A percentage of nothing is nothing, so the
fraction is 0% and the right to maintain it is a right to buy 0% of every future
round.

The only reading that gives the clause commercial meaning is "the percentage the
Investor will hold immediately after conversion", which is 4.76% —
[[raw/cap-table.md#post-money-math]]. That is a rewriting exercise, not a
construction. **A definition that requires the court to substitute a different date
to make it work is void for uncertainty, and the right fails with it.**

## 2. "More favorable" is whatever the Investor says it is

§4.2 lists five categories and closes with "and additional rights" —
[[raw/side-letter.md#4-most-favored-nation]]. "Additional rights" has no referent:
additional to what, measured how, and does a right the Company gives a strategic
partner count as an "issuance" trigger under §4.1? The clause never says.

Timing is equally loose. §4.1 bites on anything issued "before an Equity
Financing" — [[raw/side-letter.md#4-most-favored-nation]]. Does an Equity Financing
mean the priced round, or the first closing of it? A Safe issued the same week as
the financing sits on the line.

## 3. The survival clause survives nothing

§6.4: terminates on the earlier of an Equity Financing or a Liquidity Event
"except that then-surviving information-rights periods, if any, continue as
written" — [[raw/side-letter.md#6-miscellaneous]]. §3.1 sets no periods, only
delivery obligations. So "periods, if any" refers to nothing, and the clause that
is supposed to end the reporting duty may not end it, because the exception has no
content to limit it.

## 4. Two clauses answer the same question

§5.1 says the letter and the Safe together are the entire agreement —
[[raw/side-letter.md#5-conflict-entire-agreement]]. §1.2 says the letter amends the
Safe — [[raw/side-letter.md#1-recitals]]. An amending instrument and an entire
agreement clause are different mechanisms with different consequences for anything
not mentioned. §5.2 then says the letter controls, without saying whether it
controls the Safe's own definitions. If "Company Capitalization" in the letter
means something different from "Company Capitalization" in the Safe, which one
governs a conversion?

## 5. Cap math — clean

Every term used in the arithmetic is defined in §1 — [[raw/safe.md#1-definitions]].
I could not manufacture an ambiguity here, and I tried.

## What I would change first

Rewrite §2.2 to a number: "the percentage obtained by dividing the number of
shares issuable on conversion of the Safe by the Company Capitalization as of the
date of the applicable issuance". Delete "additional rights" from §4.2. Delete the
survival exception in §6.4.

## One caveat on my own conclusion

My §1 conclusion states the definition is void. That is the conclusion I believe is
right on the text, but a court asked to void a clause in a document it is being
asked to enforce will usually prefer to construe it, particularly where the drafter
was the party now relying on it. Treat the ranking as certain and the remedy as
likely to be softer than I put it.
