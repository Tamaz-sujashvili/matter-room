# Log

Append-only. Never edit an earlier entry.

## [2026-11-18] create | Halden matter scaffolded
Raw corpus placed. SHA256 stamps still PENDING. No L2 pages. No council.

## [2026-11-18] ingest | 8 sources stamped, 2 bodies fixed before the run opened

Stamped `sha256` on all 8 `raw/` bodies via `scripts/stamp_sources.py` (new).
Two sources had structural defects that would have produced citations to
headings that do not exist. Both were fixed, re-stamped, and recorded here with
both hashes rather than edited quietly:

- `raw/term-sheet.md` — 9 table rows were written as `[[row-*]]` wikilinks, which
  pointed at anchors that never existed and would render as broken links.
  Changed to code spans (`row-pro-rata`). Row names now cited in prose.
  before `fcd67cca2e38e5921f3d76be0dc85fc67dcb16bd2f792dedb4b27e7085769941`
  after  `513c588a65277adb971549d7899ec4e579f4852ff2d32535ff0cfb59bb6f873a`
- `raw/cap-table.md` — `[[post-money-math]]` and `[[option-pool]]` were inline
  link markers, not headings, so the anchors the pack recommends did not exist.
  Promoted to `### Post-money math` and `### Option pool`.
  before `84f1acecfa2e287ea0415c9b43bbf5ff5b194068f66b8b60be33a103486266a4`
  after  `399e34cfae8f99f23442c6079afaa8474cd43408eb5ba9ba830c7947665202a9`

Both files are now frozen. Any further body change fails lint as SHA drift.

## [2026-11-18] compile | 13 L2 pages

4 entities, 5 concepts, 2 comparisons, 2 queries. Every page has frontmatter, at
least 2 outbound wikilinks, and at least one `[[raw/...]]` locator on every
factual claim. Contested facts carry two sources and both readings.

Two drafting errors were caught and fixed during compile, before the council:
pro rata duration was described as "wider than Series Seed" when the widening is
in scope (any issuance of Capital Stock), and a claim about the founder's silence
on 13 Nov was unsupported by any document. Both corrected in place at compile
time; the memo never carried them.

## [2026-11-18] risk-rank | top 5

`queries/risk-rank-top-5.md`. Order: MFN, information rights, pro rata, conflict
clause, cap math. §5.2 ranks fourth on exposure because its damage is derivative —
it multiplies the first three rather than adding exposure of its own.

## [2026-11-18] council | 4 seats + anonymized review + chairman

`council/00-brief.md` through `06-chairman.md`. Four independent passes on the same
five clauses, no seat shown another's output. Stage 2 relabelled the outputs A–D
and ranked them: missing terms first, consistency second, risk third, ambiguity
fourth. Four disagreements were carried into the memo rather than resolved:
§6.2 validity, §2.2 void versus unconstruable, clause ranking, and the order of
concessions.

Chairman added one point no seat raised: 20 November is a request, not a deadline.

## [2026-11-18] deliver | 5 files

`research_memo.md`, `redline.md` (10 changes, side letter only), `fact_timeline.md`,
`evidence_index.md`, `verification_log.md`. Index updated. The YC Safe was
issue-spotted, never redlined.

## [2026-11-18] verify | 8 claims: 7 verified, 1 corrected

Row 8 corrected: the memo claimed counsel had "offered to narrow" the MFN to
Safes. Email 04 offers to *consider* and says "I'm not promising we'll agree".
Memo §3.2 amended; correction log added at §7. The chairman transcript was left
as written — the error originated there and editing it would hide the trail.

Human sign-off block in the log is deliberately blank. The memo is not verified
until it is initialled.

## [2026-11-18] lint | 0 errors, 0 warnings, 0 info

Added a fourth legal check: `bad-anchor`. It failed its first run — 8 citations to
`#post-money-math` and `#option-pool` in the cap table, which had no such
headings. That is the check paying for itself on the first matter.
