# Evidence index — Halden / Meridian

> One row per raw file. SHA256 is of the body below frontmatter, stamped at ingest
> on 18 Nov 2026 by `scripts/stamp_sources.py`. 8 sources, 2,636 words, 338 lines.
> Re-run `python3 scripts/lint_matter.py examples/halden-safe` to test for drift.

| File | SHA256 | Lines | Supports | Contradicts | Notes |
|---|---|---|---|---|---|
| [[raw/safe.md]] | `554d92bf3e709f2f604b25c44611ad12d3b3ba9f4b88deb0fafc95726c2a89c2` | 85 | Executed terms: $400k, $8M cap, no discount, Purchase Date 10 Nov. Silence on pro rata, information rights and MFN. Integration and amendment clauses. Cap arithmetic inputs | — (it is the baseline every other document is measured against) | Working copy of the public YC Post-Money Safe. Not redlined, not amended |
| [[raw/side-letter.md]] | `d99148d29690a18599df6c287e38ccf6cb86313fe0cbe6027fbebc38a722058c` | 67 | The three investor adds: pro rata §2, information rights §3, MFN §4. The precedence clause §5.2 and the amendment recital §1.2 | §4.1 contradicts the term sheet's MFN scope. §3.1 contradicts the term sheet's information-rights timing. §5.1 contradicts §1.2 internally | Draft 16 Nov, unexecuted. Object of the redline |
| [[raw/term-sheet.md]] | `513c588a65277adb971549d7899ec4e579f4852ff2d32535ff0cfb59bb6f873a` | 35 | The 28 Oct commercial deal: cap, amount, no discount, pro rata until Series Seed, info rights at Series Seed, MFN on Safes, no board seat, 30 Nov outside date | §2.1 of the letter (scope), §3.1 (timing), §4.1 (notes) | Non-binding except confidentiality and expenses. Superseded by the Safe's integration clause |
| [[raw/email-01.md]] | `57b91f6c466287d7657523359401322a91e0c76de3e6a715080052032b7b9d28` | 28 | 23 Nov funding target inside the 30 Nov outside date. Side letter described as covering "pro rata and reporting" only. Safe described as standard and unchanged | The letter as sent adds a third item (MFN over notes) beyond what this email describes | 12 Nov, counsel to founder |
| [[raw/email-02.md]] | `53c8069bccb196075c31f3bf1cfb6a36964be632d3dd49ce1be9600aa70821b8` | 24 | Counsel's 13 Nov statement that Meridian "of course" keeps pro rata and "will have it in the side letter"; "the side letter is the deal"; acknowledges the bare YC form carries no pro rata | Nothing in the executed Safe grants it — [[raw/safe.md#3-subsequent-issuances-this-instrument-is-silent]] | 13 Nov. The strongest founder-side document on intent, and it binds nothing |
| [[raw/email-03.md]] | `359aef98e4aabdc23b62daa206e3006a6c2e0c745892368698da1f4b4eadb3d4` | 28 | Founder's refusal of a pre-seed reporting covenant; offer of a voluntary monthly update; her request to know whether MFN reaches notes; her statement that the cap is not being reopened | Counsel's later characterisation of "at Series Seed" as a floor — [[raw/email-04.md#email-04-16-nov-2026]] | 14 Nov. No reply in the bundle |
| [[raw/email-04.md]] | `924c6d311fbe5f965352b193071e25b632bbd0edd3b21ab1767d933721ccc8b8` | 30 | 20 Nov signature ask; 23 Nov close; MFN widened to notes; reporting accelerated to monthly; the "6 November call" as the asserted basis | The term sheet's MFN scope and information-rights timing. The only reference to the 6 Nov call is this email | 16 Nov. Covering note for the draft |
| [[raw/cap-table.md]] | `399e34cfae8f99f23442c6079afaa8474cd43408eb5ba9ba830c7947665202a9` | 41 | 10,000,000 shares outstanding, 2,000,000 option pool, 5.00% at the cap, 4.76% after conversion, $0.80 Safe Price | Nothing — it is arithmetic derived from the Safe's definitions | Constructed. Reviewer A's input for the money analysis |

## What the index establishes

1. **Two documents are executed or signed**: the term sheet (non-binding) and the
   Safe. Everything else is a draft or an email — [[raw/term-sheet.md#other]],
   [[raw/safe.md#signature-page]].
2. **One instrument is silent where the dispute is**: the Safe grants none of the
   three rights — [[raw/safe.md#3-subsequent-issuances-this-instrument-is-silent]].
3. **Every widening runs one way**: term sheet → emails → side letter, each step
   toward the Investor. See [[deliverables/fact_timeline]].
4. **No source has drifted since ingest.** Any later edit to a `raw/` body breaks
   the SHA256 and fails lint — which is the point.

## Sources that would change the analysis

Not in the bundle, and named so the gap is visible rather than assumed away:

- the Company's charter and bylaws (does granting an MFN need board approval?)
- the full 6 November call record, if one exists —
  [[raw/email-04.md#email-04-16-nov-2026]]
- any prior side letter between these parties
- the equity incentive plan (does the pool already include a top-up obligation?)
