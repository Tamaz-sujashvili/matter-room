# Verification log — Halden / Meridian

> Eight claims sampled 18 Nov 2026 from [[deliverables/research_memo]]. Each row
> quotes the source text beside the claim so the comparison can be checked without
> reopening the file.
>
> **Who filled this:** the agent produced the claims, the locators and the quotations,
> and marked its own first-pass verdict. The verdict is a comparison, not an
> endorsement — a claim can quote correctly and still be bad law.
>
> **Sign-off is blank on purpose.** See the sign-off block at the end. The memo may
> not be described as verified until a human has initialled each row.

| # | Claim in the memo | Locator | Quoted source | Verdict | Note |
|---|---|---|---|---|---|
| 1 | The Safe issues 500,000 shares at the $8M cap, which is 4.76% of the post-conversion total, not the 5.00% headline | [[raw/cap-table.md#post-money-math]] | "Implied ownership at the cap: $400,000 / $8,000,000 = **5.00%**" … "That 500,000 / 10,500,000 ≈ **4.76% of the then-outstanding**" | verified | Both numbers are in the source. Re-derived: 8,000,000 ÷ 10,000,000 = 0.80; 400,000 ÷ 0.80 = 500,000; 500,000 ÷ 10,500,000 = 0.047619. The cap table is constructed, so this verifies the arithmetic, not an external fact |
| 2 | Safe §6.2 supersedes prior agreements and term sheets, so it does not reach a letter signed ten days later | [[raw/safe.md#6-miscellaneous]] | "This Safe … constitutes the entire agreement between the parties with respect to the subject matter hereof and supersedes all **prior** agreements, understandings, term sheets, and negotiations, whether written or oral" | verified | "Prior" is in the text. The conclusion drawn from it is construction, not quotation — a court could still read §6.2 as reaching a contemporaneous side letter. Confidence high, not certain |
| 3 | The draft MFN reaches convertible notes, which the term sheet did not | [[raw/side-letter.md#4-most-favored-nation]] | "the Company issues any subsequent Safe **or convertible promissory note** with terms more favorable to the holder than the Safe" | verified | Term sheet row reads "**MFN on subsequent Safes** (notes not mentioned)" — [[raw/term-sheet.md#investment]]. The widening is in the text, not inferred |
| 4 | Counsel stated in writing on 13 November that pro rata was granted "of course" | [[raw/email-02.md#email-02-13-nov-2026]] | "of course Meridian keeps pro rata going forward — that is standard for a $400k lead. You will have it in the side letter so there is no ambiguity at the Series Seed." | verified | Quoted correctly. It is evidence of intent only: the Safe grants no such right — [[raw/safe.md#3-subsequent-issuances-this-instrument-is-silent]] |
| 5 | The 20 November signature date is a request, not a contractual deadline; the only outside date (30 November) is non-binding | [[raw/email-04.md#email-04-16-nov-2026]] | "If the side letter isn't signed by Friday 20 November, I need a reason, because Monday is a wire day, not a negotiation day." | verified | Term sheet header: "signed by both parties as a non-binding term sheet (confidentiality and expenses binding)" — [[raw/term-sheet.md#investment]]. No signed document names 20 November. The word "request" is my characterisation; the absence of any contractual language is in the text |
| 6 | The Safe grants no pro rata, no information rights and no MFN before conversion | [[raw/safe.md#3-subsequent-issuances-this-instrument-is-silent]] | "This Safe does not, by its terms, grant the Investor pro rata rights, preemptive rights, information rights, or a most-favored-nation right in respect of subsequent issuances." | verified | §4 adds "no information rights, and no inspection rights, except as required by law" — [[raw/safe.md#4-no-stockholder-rights]]. This is the load-bearing claim of the memo and it is in terms |
| 7 | Conversion is at the lower of the financing price or the Safe Price, and the Safe Price is the cap divided by Company Capitalization | [[raw/safe.md#2-purchase-conversion]] | "at a conversion price equal to the lower of (i) the price per share of the Capital Stock sold in the Equity Financing, and (ii) the Safe Price" | verified | §1.7: "**'Safe Price'** means the Post-Money Valuation Cap divided by the Company Capitalization" — [[raw/safe.md#1-definitions]]. §1.3 puts the Unissued Option Pool inside Company Capitalization and excludes this Safe |
| 8 | Counsel has offered to narrow §4.1 to Safes if the Company asks in one sentence, which closes the MFN gap | [[raw/email-04.md#email-04-16-nov-2026]] | "If you want the MFN limited to Safes, say so in one sentence and we'll consider it — **I'm not promising we'll agree**." | **corrected** | The memo said counsel had "offered to narrow" the clause. The text is an offer to *consider*, with an express refusal to commit. Consequence: the MFN gap is open, not closed, and closing it is a negotiation. Memo §3.2 amended; see the correction log in [[deliverables/research_memo]] §7 |

## What the correction changed

| Where | Before | After |
|---|---|---|
| Memo §3.2 | "Counsel has already offered to narrow §4.1 to Safes if the Company asks in one sentence … so the MFN gap is the cheapest of the three to close" | "Counsel has offered to **consider** narrowing §4.1 to Safes … and expressly declined to commit. The gap is open, not closed" |
| Memo §4 sequencing | Implied the MFN narrowing was available on request | 3 and 4 are a negotiation, not a formality |
| Memo §5 open items | Did not list Investor acceptance as unknown | Unchanged — already listed as unknown and commercial |

**Not changed:** `council/06-chairman.md` still records the concession finding as
the chairman wrote it. A transcript that is edited after the fact is worth less than
one that is wrong in public. The error and its correction live in the memo and here.

**Why this row matters more than the other seven.** Seven rows confirm the memo read
the files correctly. Row 8 shows the memo misread an opposing party's position in the
direction that made the client's week easier. That is the failure mode a citation
rule cannot catch, and the only reason this log is worth publishing.

## Claims deliberately not sampled

- "Nothing in the term sheet binds her" — true but rests on the non-binding header,
  already covered by row 5.
- "The side letter would override the Safe" — a construction of §5.2, not a fact to
  verify. Covered in the memo as an assessment.
- Any statement about Delaware law. Nothing in the bundle is authority, and nothing
  in the memo asserts a rule of law that a statute or case would confirm.
- The 6 November call. No record exists; row 5's email is the only reference, and the
  memo treats the call as unproven.

## Human sign-off

Initial each row after re-reading the quoted text. Do not initial a row you have not
reopened.

| # | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Initials |  |  |  |  |  |  |  |  |
| Date |  |  |  |  |  |  |  |  |

Verdicts used: `verified` · `corrected` · `could not verify` · `pending`.
