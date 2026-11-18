# Verification log — Halden / Meridian

> Eight claims sampled 18 Nov 2026 from [[deliverables/research_memo]]. Each row
> quotes the source text beside the claim so the comparison can be checked without
> reopening the file.
>
> **Two columns, two authors.** `Agent check` records whether the quotation in the
> memo matches the cited file — a mechanical comparison the agent can make and is
> allowed to state. `Human verdict` is the legal judgement, and every row is
> `pending` because the agent does not fill it. Seven rows match. One does not, and
> the memo was corrected (see the correction table below).

| # | Claim in the memo | Locator | Quoted source | Agent check | Human verdict |
|---|---|---|---|---|---|
| 1 | The Safe issues 500,000 shares at the $8M cap, which is 4.76% of the post-conversion total, not the 5.00% headline | [[raw/cap-table.md#post-money-math]] | "Implied ownership at the cap: $400,000 / $8,000,000 = **5.00%**" … "That 500,000 / 10,500,000 ≈ **4.76% of the then-outstanding**" | quotes match · arithmetic re-derived | pending |
| 2 | Safe §6.2 supersedes prior agreements and term sheets, so it does not reach a letter signed ten days later | [[raw/safe.md#6-miscellaneous]] | "This Safe … constitutes the entire agreement between the parties with respect to the subject matter hereof and supersedes all **prior** agreements, understandings, term sheets, and negotiations, whether written or oral" | quotes match · "prior" is in the text; the conclusion is construction | pending |
| 3 | The draft MFN reaches convertible notes, which the term sheet did not | [[raw/side-letter.md#4-most-favored-nation]] | "the Company issues any subsequent Safe **or convertible promissory note** with terms more favorable to the holder than the Safe" | quotes match · term sheet row reads "MFN on subsequent Safes (notes not mentioned)" | pending |
| 4 | Counsel stated in writing on 13 November that pro rata was granted "of course" | [[raw/email-02.md#email-02-13-nov-2026]] | "of course Meridian keeps pro rata going forward — that is standard for a $400k lead. You will have it in the side letter so there is no ambiguity at the Series Seed." | quotes match · intent only; the Safe grants nothing | pending |
| 5 | The 20 November signature date is a request, not a contractual deadline; the only outside date (30 November) is non-binding | [[raw/email-04.md#email-04-16-nov-2026]] | "If the side letter isn't signed by Friday 20 November, I need a reason, because Monday is a wire day, not a negotiation day." | quotes match · no signed document names 20 November; term sheet is non-binding | pending |
| 6 | The Safe grants no pro rata, no information rights and no MFN before conversion | [[raw/safe.md#3-subsequent-issuances-this-instrument-is-silent]] | "This Safe does not, by its terms, grant the Investor pro rata rights, preemptive rights, information rights, or a most-favored-nation right in respect of subsequent issuances." | quotes match · §4 adds "no information rights, and no inspection rights, except as required by law" | pending |
| 7 | Conversion is at the lower of the financing price or the Safe Price, and the Safe Price is the cap divided by Company Capitalization | [[raw/safe.md#2-purchase-conversion]] | "at a conversion price equal to the lower of (i) the price per share of the Capital Stock sold in the Equity Financing, and (ii) the Safe Price" | quotes match · §1.7 defines Safe Price as cap ÷ Company Capitalization | pending |
| 8 | Counsel has offered to narrow §4.1 to Safes if the Company asks in one sentence, which closes the MFN gap | [[raw/email-04.md#email-04-16-nov-2026]] | "If you want the MFN limited to Safes, say so in one sentence and we'll consider it — **I'm not promising we'll agree**." | **mismatch** · memo said "offered to narrow"; the text offers to *consider* and refuses to commit. Memo §3.2 corrected | pending |

## Correction 8 — what changed

| Where | Before | After |
|---|---|---|
| Memo §3.2 | "Counsel has already offered to narrow §4.1 to Safes … so the MFN gap is the cheapest of the three to close" | "Counsel has offered to **consider** narrowing §4.1 to Safes … and expressly declined to commit. The gap is open, not closed" |
| Memo §4 | Implied the MFN narrowing was available on request | Changes 3 and 4 are a negotiation, not a formality |
| Memo §7 | — | Correction log added, with the consequence stated |

**Not changed:** `council/06-chairman.md` still records the concession finding as the
chairman wrote it. A transcript edited after the fact is worth less than one that is
wrong in public. The error and its correction live in the memo and here.

**Why this row matters more than the other seven.** Seven rows confirm the memo read
the files correctly. Row 8 shows it misread an opposing party's position in the
direction that made the client's week easier. That is the failure mode a citation
rule cannot catch, and it is the only reason this log is worth publishing.

## Claims deliberately not sampled

- "Nothing in the term sheet binds her" — true, but it rests on the non-binding
  header, already covered by row 5.
- "The side letter would override the Safe" — a construction of §5.2, not a fact to
  verify. Carried in the memo as an assessment.
- Any statement about Delaware law. Nothing in the bundle is authority, and the memo
  asserts no rule of law that a statute or case would confirm.
- The 6 November call. No record exists; row 5's email is the only reference, and the
  memo treats the call as unproven.

## Human sign-off

Read the claim, open the locator, read the quoted line in the source, then write
`verified`, `corrected` or `could not verify`. Do not initial a row you have not
reopened. Row 8 is the correction — check the quotation, then check that the memo
now says what the quotation says.

| # | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Verdict | pending | pending | pending | pending | pending | pending | pending | pending |
| Initials |  |  |  |  |  |  |  |  |
| Date |  |  |  |  |  |  |  |  |

Verdicts: `verified` · `corrected` · `could not verify` · `pending`.
