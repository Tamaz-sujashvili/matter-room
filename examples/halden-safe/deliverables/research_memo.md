# Research memo — Halden Analytics pre-close review

> Live question: what does the founder actually owe on Monday, what gets redlined
> in the side letter before Friday, and what stays off the Safe?
> Date: 2026-11-18
> Status: council-merged · agent verification pass: 7 verified, 1 corrected ·
> human sign-off pending on [[deliverables/verification_log]]
> Council: seat A risk · seat B missing · seat C consistency · seat D ambiguity · chairman
> Matter is **constructed and fictional**. No client data.

## 1. Question

Halden Analytics, Inc. executed a YC Post-Money Safe with Meridian Ventures I, L.P.
on 10 November 2026: $400,000, $8,000,000 post-money cap, no discount —
[[raw/safe.md#1-definitions]]. Close is Monday 23 November. Before then the Company
must decide whether to sign a side letter, drafted 16 November and still unexecuted,
that adds pro rata rights, monthly information rights, and an MFN —
[[raw/side-letter.md#1-recitals]].

The three additions are not new asks. The term sheet carried a narrower version of
two of them and excluded the third — [[raw/term-sheet.md#investment]]. Counsel says
in writing that "the side letter is the deal" — [[raw/email-02.md#email-02-13-nov-2026]].
The founder said in writing that she would not take a reporting covenant at pre-seed
— [[raw/email-03.md#email-03-14-nov-2026]].

## 2. Short answer

Today she owes what the Safe says and nothing else: $400,000 converting at the lower
of the financing price or the Safe Price, with no pro rata right, no information
right, and no MFN — [[raw/safe.md#3-subsequent-issuances-this-instrument-is-silent]].
Nothing in the term sheet or the emails binds her, because the term sheet is
non-binding and the Safe supersedes every prior understanding in terms —
[[raw/safe.md#6-miscellaneous]].

A side letter signed on Friday **will** bind her, and will override the Safe wherever
it says it controls — [[raw/side-letter.md#5-conflict-entire-agreement]]. So the
redline is the negotiation, and three changes carry it: delete §5.2, narrow the MFN
to Safes, and fix pro rata's scope and mechanics. Nothing is added to the Safe
itself: it is a market-standard form, it is already executed, and every
investor-specific right belongs in the letter.

## 3. What the documents say

### 3.1 The gate: which document governs

- **What it is:** a conflict between two integration clauses.
- **Risk:** high.
- **Documents:**
  - [[raw/safe.md#6-miscellaneous]] — the Safe "supersedes all prior agreements,
    understandings, term sheets, and negotiations, whether written or oral".
  - [[raw/safe.md#6-miscellaneous]] — amendable "only by a writing signed by the
    Company and the Investor".
  - [[raw/side-letter.md#5-conflict-entire-agreement]] — "this Side Letter shall
    control".
  - [[raw/side-letter.md#1-recitals]] — the letter is intended to "amend and
    complement" the Safe.
- **Council:** Reviewer C (consistency) reads §6.2 as extinguishing the letter,
  because the letter papers a 6 November understanding and so is itself a prior
  understanding. The chairman rejects that reading and Reviewer A did not raise it.
- **Assessment:** §6.2 is temporal. It reaches what came before it — the 28 October
  term sheet and the 6 November call — and a letter signed on 20 November is not
  before it. A signed letter is effective, and it is effective by the route §6.3
  supplies. The consistency seat's reading would make its own §5.2 analysis
  unreachable, which is a sign it is wrong.
- **Action:** keep §1.2; delete §5.2 and replace it with precedence limited to the
  provisions the letter actually addresses. Redline change 1.

### 3.2 MFN — the clause that can move the price

- **What it is:** a right, currently unbounded in scope.
- **Risk:** high.
- **Documents:**
  - [[raw/side-letter.md#4-most-favored-nation]] — applies to any subsequent Safe
    **or convertible promissory note**; "more favorable" includes "additional rights".
  - [[raw/term-sheet.md#investment]] — MFN on subsequent **Safes**; notes not
    mentioned.
  - [[raw/email-03.md#email-03-14-nov-2026]] — the founder flagged the note risk
    before the draft arrived.
  - [[raw/email-04.md#email-04-16-nov-2026]] — counsel confirms the widening and
    grounds it on "the 6 November call".
- **Council:** Reviewer A ranks this first on exposure and is right; Reviewer B
  agrees but adds that the clause has no notice or election mechanics.
- **Assessment:** this is the only clause in the bundle that can change the price of
  a future round without a signature. With §4.1 as drafted, a bridge note at a lower
  cap automatically resets Meridian's $8M cap, and §4.2's "additional rights" imports
  any term given to any later investor — [[raw/side-letter.md#4-most-favored-nation]].
  The 6 November call cannot carry the term: it is exactly what §6.2 supersedes —
  [[raw/safe.md#6-miscellaneous]]. Counsel has offered to **consider** narrowing
  §4.1 to Safes if the Company asks in one sentence, and expressly declined to
  commit — "I'm not promising we'll agree" — [[raw/email-04.md#email-04-16-nov-2026]].
  So the gap is open, not closed: closing it is a negotiation, not a formality.
  (Corrected in verification. See §7.)
- **Action:** delete "or convertible promissory note" from §4.1 and "and additional
  rights" from §4.2; add a notice duty. Redline changes 3, 4, 5.

### 3.3 Pro rata — the clause that costs years

- **What it is:** a right, wider in scope than anything agreed, with unusable
  mechanics.
- **Risk:** high.
- **Documents:**
  - [[raw/side-letter.md#2-pro-rata-rights]] — any subsequent "issuance of Capital
    Stock"; Pro Rata Share measured from "the date of this Side Letter"; exercise
    "as reasonably agreed".
  - [[raw/term-sheet.md#investment]] — pro rata "in subsequent Safes until Series Seed".
  - [[raw/safe.md#4-no-stockholder-rights]] — on 16 November the Investor held no
    shares and had no rights.
- **Council:** Reviewer B ranks this first on repair priority, not exposure, and
  Reviewer D calls the definition void. The chairman keeps the ranking distinction
  and rejects the voidness conclusion: the definition is unworkable, and it would be
  construed against the party that drafted it.
- **Assessment:** the right is normal for a $400k lead and the founder never disputed
  it — her 14 November email challenges only reporting and MFN —
  [[raw/email-03.md#email-03-14-nov-2026]]. What is not normal is a right over "any
  issuance of Capital Stock" with no carve-out: read literally it reaches every
  option grant and every conversion. Add to that a numerator that computes to zero,
  no stated price, and no exercise window, and the clause cannot be operated in a
  closing calendar.
- **Action:** add carve-outs for plan issuances, conversions and acquisitions; state
  the price as the price paid by the new investors; fix the denominator to the
  post-conversion percentage; set a 15-day election window. Redline changes 6–8.

### 3.4 Information rights — the clause worth trading

- **What it is:** a reporting covenant with no end and no confidentiality.
- **Risk:** high.
- **Documents:**
  - [[raw/side-letter.md#3-information-rights]] — monthly statements within 15 days,
    annual budget, "such other information as the Investor may reasonably request",
    plus inspection rights.
  - [[raw/safe.md#4-no-stockholder-rights]] — no information or inspection rights
    before conversion.
  - [[raw/term-sheet.md#investment]] — "at Series Seed (not before)".
  - [[raw/email-03.md#email-03-14-nov-2026]] — the founder's refusal of a pre-seed
    covenant, and her offer of a voluntary update.
  - [[raw/side-letter.md#6-miscellaneous]] — termination "except that then-surviving
    information-rights periods, if any" survive.
- **Council:** Reviewer B catches the vacuity of that survival wording; Reviewer C
  notes the Company never replied to its own stated position.
- **Assessment:** the founder's instinct is commercially sound and contractually
  irrelevant — she argued from a non-binding term sheet, and counsel answered by
  calling it a floor — [[raw/email-04.md#email-04-16-nov-2026]]. The cost is
  attention, not dollars, so this is the clause to trade rather than fight: take
  monthly reporting if the MFN narrows, but only with a confidentiality clause and a
  sunset.
- **Action:** add confidentiality and a sunset; either make the monthly update
  expressly non-contractual or accept a quarterly package. Redline change 9.

### 3.5 Cap math — correct, and not to be touched

- **What it is:** conversion arithmetic under the Safe's own definitions.
- **Risk:** low.
- **Documents:**
  - [[raw/safe.md#1-definitions]] — Safe Price = cap ÷ Company Capitalization;
    Company Capitalization includes the Unissued Option Pool and excludes Safes and
    notes.
  - [[raw/cap-table.md#post-money-math]] — $8,000,000 ÷ 10,000,000 = $0.80;
    $400,000 ÷ $0.80 = 500,000 shares; 500,000 ÷ 10,500,000 = 4.76%.
- **Council:** no seat disputed the arithmetic; Reviewer A asked only that the founder
  fix her dilution model.
- **Assessment:** 5.00% is Purchase Amount ÷ Cap, measured against a base the Safe is
  excluded from. The stake actually issued is 4.76%. The gap is not a drafting error
  and no redline would change it. Issue-spot, do not amend.
- **Action:** model dilution at 4.76%; decide the option pool size before the priced
  round, since the pool sits inside Company Capitalization.

## 4. Recommended redline set

Side letter only. Change numbers match [[deliverables/redline]].

| # | Change | Why | Reviewer | Source |
|---|---|---|---|---|
| 1 | Delete §5.2; replace with precedence limited to the provisions addressed | A later letter should not win every unaddressed argument | C | [[raw/side-letter.md#5-conflict-entire-agreement]] |
| 2 | §1.2: "amend and complement" → "supplement the Safe only as expressly provided in this letter" | Removes the §1.2 / §5.1 contradiction | C, D | [[raw/side-letter.md#1-recitals]] |
| 3 | §4.1: delete "or convertible promissory note" | Removes the bridge-note reset | A | [[raw/side-letter.md#4-most-favored-nation]] |
| 4 | §4.2: delete "and additional rights" | Stops the clause importing every future side letter | A, D | [[raw/side-letter.md#4-most-favored-nation]] |
| 5 | §4.1: add notice duty and written confirmation of improved terms | The Company currently cannot know when it has triggered | B | [[raw/side-letter.md#4-most-favored-nation]] |
| 6 | §2.1: carve out plan issuances, conversions, acquisitions | Otherwise every option grant is a notice event | B | [[raw/side-letter.md#2-pro-rata-rights]] |
| 7 | §2.2: replace circular definition with post-conversion percentage; add price | The current numerator is zero and the price is unstated | B, D | [[raw/side-letter.md#2-pro-rata-rights]] |
| 8 | §2.3: 15 business days' notice, 15-day election window | "As reasonably agreed" cannot be operated | B | [[raw/side-letter.md#2-pro-rata-rights]] |
| 9 | §3: add confidentiality; add a 24-month sunset; drop "such other information" | A covenant with no end and no confidence is the worst combination | B, C | [[raw/side-letter.md#3-information-rights]] |
| 10 | §6.4: delete the "then-surviving information-rights periods, if any" exception | The exception refers to a period §3 never sets | B, D | [[raw/side-letter.md#6-miscellaneous]] |

Sequence matters: change 1 first, then 3 and 4, then 6–9. Reviewer A proposed
trading reporting for MFN scope immediately; Reviewer C objected that §5.2 makes
every concession permanent. The chairman adopts the objection — same trade, later.

## 5. What we did not decide

- **Whether the Company needs a board consent** to grant pro rata or an MFN. The
  bundle has no charter, no bylaws, and no board minutes, so this memo cannot say.
  This is the first thing to check before signature.
- **Whether a 4.76% holder is a "Major Investor"** under any existing instrument.
  Nothing in the bundle defines the term; only the term sheet uses it —
  [[raw/term-sheet.md#investment]].
- **Whether the 6 November call happened as described.** There is no written record
  of it in the bundle — [[raw/email-04.md#email-04-16-nov-2026]]. This memo treats it
  as unproven and, for the reasons in §3.1, as superseded either way.
- **Delaware authority on construing a circular percentage definition.** Not
  researched here. The recommendation to fix the text does not depend on it.
- **Whether the Investor will sign a letter with §5.2 removed.** Unknown, and the
  answer is commercial, not legal.

## 6. Verification pointer

Eight claims sampled in [[deliverables/verification_log]], each with its locator and
the quoted source text. Seven verified on a first pass and one was corrected. This
memo may not be called verified until a human has initialled those rows.

## 7. Correction log

One claim in the first draft was wrong, and it was wrong in the direction that made
the week easier.

- **Draft said:** counsel had already offered to narrow §4.1 to Safes if the Company
  asked, so the MFN gap was the cheapest of the three to close.
- **The source says:** "If you want the MFN limited to Safes, say so in one sentence
  and we'll consider it — I'm not promising we'll agree" —
  [[raw/email-04.md#email-04-16-nov-2026]].
- **Corrected text** now reads that counsel offered to consider, and declined to
  commit, in §3.2 above.
- **Consequence:** the MFN narrowing moves from "available on request" to "open
  negotiation". Redline changes 3 and 4 lose the assumption that the Investor has
  already conceded them.
- **Record:** [[deliverables/verification_log]] row 8. The council transcript at
  `council/06-chairman.md` is left as written — the error originated there, and an
  edited transcript would hide it.

The other seven sampled claims held. Nothing else in this memo was revised after
verification.
