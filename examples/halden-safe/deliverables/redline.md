# Redline — Meridian side letter (draft 16 Nov 2026)

> Base: [[raw/side-letter.md]] · SHA256 `d99148d29690a185…`, unstamped body unchanged
> Date: 2026-11-18
> Rule: market-standard forms are issue-spotted in the memo, not redlined here.
> The YC Safe is **not** redlined. Every change below is to the side letter.
> Marking: ~~struck~~ **inserted**. Each change names the reviewer and the source.

Changes 1–4 and 6–8 change what the Investor gets. Changes 5, 9 and 10 change what
the Company has to do. Sequence matters: take 1 first, then 3 and 4.

---

## Change 1 — §5.2 precedence

- Reviewer: C consistency
- Source: [[raw/side-letter.md#5-conflict-entire-agreement]], [[raw/safe.md#6-miscellaneous]]
- Reason: as drafted the letter wins every conflict, including conflicts over terms
  it does not address.

**Before**

> **5.2** In the event of any conflict between this Side Letter and the Safe, this
> Side Letter shall control.

**After**

~~**5.2** In the event of any conflict between this Side Letter and the Safe, this Side Letter shall control.~~

**5.2** In the event of any conflict between this Side Letter and the Safe, the
Safe shall control, except to the extent that this Side Letter expressly amends a
specifically identified provision of the Safe, and then only with respect to that
provision.

**Footnote:** this does not weaken Sections 2, 3 or 4. They grant the rights
directly; §5.2 only decides who wins a fight the parties have not had. A letter
without §5.2 still delivers everything the Investor asked for.

---

## Change 2 — §1.2 "amend and complement"

- Reviewer: C consistency, D ambiguity
- Source: [[raw/side-letter.md#1-recitals]], [[raw/side-letter.md#5-conflict-entire-agreement]]
- Reason: "amend" and §5.1's "together constitute the entire agreement" cannot both
  be true. Pick supplement.

**Before**

> **1.2** The parties intend this Side Letter to **amend and complement** the Safe
> and to set out certain additional rights of the Investor.

**After**

**1.2** The parties intend this Side Letter to ~~amend and complement~~ **supplement**
the Safe, and to set out certain additional rights of the Investor, **only as
expressly provided in this Side Letter**.

**Footnote:** "supplement" keeps §5.1 coherent. It does not give up any right in
Sections 2–4; those sections operate on their own terms.

---

## Change 3 — §4.1 MFN over convertible notes

- Reviewer: A risk
- Source: [[raw/side-letter.md#4-most-favored-nation]], [[raw/term-sheet.md#investment]]
- Reason: an MFN over notes lets a bridge with a lower cap reset this Safe's cap
  automatically. The term sheet scoped the MFN to Safes.

**Before**

> **4.1** If, before an Equity Financing, the Company issues any subsequent Safe
> **or convertible promissory note** with terms more favorable to the holder than
> the Safe, the Investor shall automatically receive those more favorable terms.

**After**

**4.1** If, before an Equity Financing, the Company issues any subsequent Safe
~~or convertible promissory note~~ with terms more favorable to the holder than the
Safe, the Investor shall automatically receive those more favorable terms.

**Footnote:** this does not remove the MFN. It limits it to the instrument the term
sheet named. A bridge note issued later can still be negotiated separately; it just
will not reset this Safe by operation of law.

---

## Change 4 — §4.2 "additional rights"

- Reviewer: A risk, D ambiguity
- Source: [[raw/side-letter.md#4-most-favored-nation]]
- Reason: "additional rights" has no referent and imports every term given to any
  later investor, including information and pro rata terms negotiated separately.

**Before**

> **4.2** "More favorable" includes, without limitation, a lower valuation cap, a
> discount, a higher interest rate, more senior repayment, and additional rights.

**After**

**4.2** "More favorable" means ~~includes, without limitation,~~ a lower valuation
cap, a discount, a higher interest rate, or more senior repayment~~, and additional
rights~~.

**Footnote:** "means" closes the list. If the Investor wants a specific right to
travel, it should be named in §4.2 — a named right is a negotiation, which is what
the Company wants.

---

## Change 5 — §4.1 notice and confirmation (new §4.3)

- Reviewer: B missing
- Source: [[raw/side-letter.md#4-most-favored-nation]]
- Reason: the clause triggers automatically with no duty to tell the Company it has
  triggered, and no mechanism to paper the improved terms.

**Before**

> *(no equivalent provision — the letter has no notice or confirmation mechanic)*

**After**

**4.3** Within ten (10) business days after any issuance described in Section 4.1,
the Company shall notify the Investor in writing and identify the terms said to be
more favorable. Improved terms take effect only when set out in a writing signed by
both parties.

**Footnote:** this does not delay the Investor's entitlement; it fixes when the
entitlement is known. Without it the Company can be in breach before anyone notices.

---

## Change 6 — §2.1 carve-outs

- Reviewer: B missing
- Source: [[raw/side-letter.md#2-pro-rata-rights]]
- Reason: §2.1 covers "any subsequent issuance of Capital Stock". With no carve-out,
  every option grant and every conversion is a notice event.

**Before**

> **2.1** The Investor shall have the right to purchase its **Pro Rata Share** of
> any subsequent issuance of Capital Stock by the Company, until the closing of an
> Equity Financing.

**After**

**2.1** The Investor shall have the right to purchase its **Pro Rata Share** of any
subsequent issuance of Capital Stock by the Company, until the closing of an Equity
Financing. **This Section 2.1 does not apply to (i) shares issued under the
Company's equity incentive plans, (ii) shares issued on conversion or exercise of
securities outstanding on the date of this Side Letter, (iii) shares issued in a
transaction in which the Company is acquired, or (iv) shares issued in the Equity
Financing.**

**Footnote:** carve-outs (i)–(iii) are market standard and cost the Investor nothing
it asked for. Carve-out (iv) restates the termination in the same sentence rather
than leaving it to §6.4.

---

## Change 7 — §2.2 Pro Rata Share and price

- Reviewer: B missing, D ambiguity
- Source: [[raw/side-letter.md#2-pro-rata-rights]], [[raw/safe.md#4-no-stockholder-rights]]
- Reason: the current fraction is measured from a date on which the Investor owns
  nothing, so it computes to zero; and no price is stated anywhere.

**Before**

> **2.2** "Pro Rata Share" means the fraction the Investor would need to maintain
> its percentage ownership of the Company **as of the date of this Side Letter**.

**After**

**2.2** "Pro Rata Share" means the quotient obtained by dividing (i) the number of
shares of Capital Stock issuable to the Investor on conversion of the Safe
immediately before the applicable issuance, by (ii) the Company Capitalization
immediately before the applicable issuance. **The purchase price for shares
purchased under Section 2.1 shall be the price per share paid by the purchasers in
the applicable issuance.**

**Footnote:** this makes the right computable and prices it at the round price. It
does not give the Investor a discount, and it does not change the conversion
arithmetic in the Safe.

---

## Change 8 — §2.3 notice and election window

- Reviewer: B missing
- Source: [[raw/side-letter.md#2-pro-rata-rights]]
- Reason: "as reasonably agreed" is not a period. A right with no clock cannot be
  exercised against a closing.

**Before**

> **2.3** The Company shall give the Investor **written notice** of any such
> issuance. The Investor shall have a period of time to exercise, as reasonably
> agreed.

**After**

**2.3** The Company shall give the Investor **written notice** of any such issuance
at least **fifteen (15) business days** before the anticipated closing. The Investor
may exercise by written notice **within fifteen (15) days after receipt**, failing
which the right lapses as to that issuance only~~. The Investor shall have a period
of time to exercise, as reasonably agreed~~.

**Footnote:** "lapses as to that issuance only" is the part worth keeping: a missed
window does not kill the right for later rounds.

---

## Change 9 — §3.1 scope, confidentiality, sunset

- Reviewer: B missing, C consistency
- Source: [[raw/side-letter.md#3-information-rights]], [[raw/safe.md#4-no-stockholder-rights]]
- Reason: the covenant runs from signature with no end, no confidentiality clause,
  and an open-ended request right — the worst combination available at pre-seed.

**Before**

> **3.1** Beginning on the date of this Side Letter, the Company shall deliver to
> the Investor:
> - (a) **monthly** unaudited financial statements within fifteen (15) days after month-end;
> - (b) an annual budget, approved by the board, before each fiscal year; and
> - (c) such other information as the Investor may reasonably request.

**After**

**3.1** Beginning on the date of this Side Letter **and ending on the earlier of
the closing of an Equity Financing or the twenty-four (24) month anniversary of
this Side Letter**, the Company shall deliver to the Investor:

- (a) **quarterly** unaudited financial statements within **thirty (30)** days after quarter-end;
- (b) an annual budget, approved by the board, before each fiscal year~~; and~~
~~- (c) such other information as the Investor may reasonably request~~.

**3.3** The Investor shall keep all information received under this Section 3
confidential, shall use it only to monitor its investment, and shall not disclose
it except to its affiliates, advisers and limited partners bound by equivalent
obligations, or as required by law.

**Footnote:** this trades frequency for duration — quarterly for 24 months instead
of monthly forever. If the Investor insists on monthly, keep monthly and hold the
sunset and §3.3. Do not give up both.

---

## Change 10 — §6.4 survival exception

- Reviewer: B missing, D ambiguity
- Source: [[raw/side-letter.md#6-miscellaneous]]
- Reason: the exception preserves "then-surviving information-rights periods, if
  any". §3 sets no periods, so the exception refers to nothing.

**Before**

> **6.4** This Side Letter terminates on the earlier of an Equity Financing or a
> Liquidity Event, except that then-surviving information-rights periods, if any,
> continue as written.

**After**

**6.4** This Side Letter terminates on the earlier of an Equity Financing or a
Liquidity Event~~, except that then-surviving information-rights periods, if any,
continue as written~~, **except that Section 3 survives for the period stated in
Section 3.1 and Section 3.3 survives indefinitely.**

**Footnote:** the only intended survivor is confidentiality. Naming it removes the
argument that reporting outlives the letter.

---

## What this redline does not do

- It does not touch the Safe. The Safe is a market-standard form and is already
  executed — [[raw/safe.md#6-miscellaneous]].
- It does not renegotiate the cap, the discount, or the purchase amount —
  [[raw/term-sheet.md#investment]].
- It does not add a board seat, a veto, or a dividend. Nobody asked for one.
- It does not decide whether the Investor will accept any of it. See
  [[deliverables/research_memo]] §5.
