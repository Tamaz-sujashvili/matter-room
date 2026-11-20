# Lovable build prompt — Matter Room page

Paste the block below into a new Lovable project, then publish to
`matter-room.lovable.app`. Lovable cannot import this repository: its git sync
exports from Lovable only, so the page is rebuilt here and the copy is fixed in
advance. `docs/index.html` stays the source of truth for the words.

After it publishes, send the URL back so the submission form and `SUBMISSION.md`
can point at it, and check the page logged out against the list at the bottom.

---

Build a single-page static site. No backend, no database, no auth, no forms, no
analytics, no newsletter block. One route. It must render as a document, not as a
SaaS landing page.

## What it is

Matter Room is a skill an agent reads. It turns a folder of contracts and emails
into a cited matter file and, when a signature is pending, a one-page closing brief.
The page is the public artifact for a hackathon entry in the Legal Practice track.
The matter on the page is fictional.

## Non-negotiables

- Masthead carries this line, small, above the fold:
  `Fictional matter. Halden Analytics and Meridian Ventures do not exist. Nothing here is legal advice.`
- Every outbound link goes to `https://github.com/Tamaz-sujashvili/matter-room`, and
  the six deliverable cards link to their files under
  `/blob/main/examples/halden-safe/deliverables/<name>`.
- Use the copy below verbatim. Do not add statistics, testimonials, logos, badges,
  counters, or "trusted by" strips. Do not add a pricing section.
- The only numbers allowed are the ones in the copy: $400,000, $8,000,000, 500,000,
  10.5M, 5.00%, 4.76%, 341, 8, 13, 6, ten, eight, 85, 280.
- Dark mode via `prefers-color-scheme`. Both modes must pass AA on body text.
- Radius 2px maximum. Hairline borders. No gradients, no glass, no drop shadows, no
  glow, no gradient text, no emoji.

## Design tokens

Light / dark pairs:

| token | light | dark | use |
|---|---|---|---|
| paper | #f7f4ec | #14120e | page background |
| card | #fffdf7 | #1b1813 | raised blocks |
| ink | #191611 | #f2ece0 | body and headings |
| ink-soft | #4f4a41 | #b6ae9c | secondary text |
| rule | #dcd5c4 | #332f26 | hairlines |
| accent | #8f1f16 | #e5988a | section numbers, links, marks |

Type: serif throughout for display and body — Iowan Old Style, Palatino, Georgia,
serif. Mono for file names, citations, section numbers and labels. Measure 68
characters. Body line-height 1.6. Headings tracking -0.02em. Section headings carry
`§ n` in mono, accent coloured, before the title.

Layout: one column, max-width about 62rem, generous vertical rhythm between
sections, a hairline above each section. The masthead is sticky with a hairline
under it. The deliverable grid is a simple 2–3 column grid on wide screens, one
column on phones.

## Sections, in order, with the exact copy

### Masthead

Wordmark `MATTER ROOM` (mono, letter-spaced, `MATTER` in ink, `ROOM` in accent).
Right side: links `Repo`, `SKILL.md`, `MIT`. Below, the small disclaimer line. Far
right, `Tamaz Sujashvili · 2026`.

### Hero

Eyebrow, mono, uppercase, letter-spaced:
`Built with AutoClaw · Round 3 · Legal Practice`

H1:
`A contract bundle in. A matter file out.`

Paragraph 1:
`Matter Room is a skill an agent reads. It hashes a folder of agreements and emails, compiles a cited wiki, ranks the five worst clauses, runs four reviewer passes on them, and drafts the redline — with every change traced to a reviewer and a source.`

Paragraph 2:
`When a signature is pending it stops early and writes the one-page closing brief first: what binds today, three edits to push, what counsel still has to confirm. Every claim about what the other side agreed to is labelled — signed term, express agreement, proposal, unresolved — and carries its quotation.`

Buttons, in this order: primary `Read the brief`, then ghost `Read the memo`, ghost
`View the run`. (A fourth, `Watch the 85 seconds`, stays hidden until a video URL
exists — render the markup but keep it hidden.)

Meta line, mono, small:
`Constructed matter · 8 sources · 13 cited pages · 6 deliverables · lint clean`

### § 1 The matter

Paragraph:
`Halden Analytics signed a $400,000 YC Post-Money Safe with Meridian Ventures at an $8,000,000 cap. Six days later, opposing counsel sent a side letter adding pro rata rights, monthly reporting and a most-favoured-nation clause. Four emails sit in the file. Close is Monday. The Company has no counsel.`

A four-cell fact strip, label in mono above value:

- `Instrument` — `YC Post-Money Safe` / `cap, no discount`
- `Purchase` — `$400,000` / `at an $8M cap`
- `Added by letter` — `Pro rata · reporting` / `MFN`
- `Close` — `Monday 23 Nov` / `no binding deadline`

Pull quote:
`The emails promise pro rata and information rights “of course”. The Safe is silent and has an entire-agreement clause. What does the founder actually owe, what gets redlined before Friday, and what stays off the Safe?`

Mono caption under it: `The live question · queries/what-does-the-founder-owe.md`

### § 2 What the run found

Three numbered findings, number in mono (`01`, `02`, `03`), each a heading, a
paragraph, and a mono source line.

01 — `The integration clause is temporal. The draft's override is the problem.`
`§6.2 supersedes prior agreements, understandings and term sheets — the 28 October term sheet and a 6 November call. It does not reach a letter signed ten days after it. So the letter binds. Which makes its own “this Side Letter shall control” the clause to delete first.`
Sources: `safe.md §6.2 · side-letter.md §5.2`

02 — `The MFN reaches convertible notes, which the term sheet never covered.`
`The term sheet said subsequent Safes. The draft says any Safe or convertible promissory note, and adds that “more favorable” includes additional rights. A $250k bridge at a lower cap then resets this Safe automatically — no notice, no election, no signature.`
Sources: `side-letter.md §4.1–4.2 · term-sheet.md`

03 — `5.00% is the headline. 4.76% is the stake.`
`$400,000 ÷ $8,000,000 is the number founders quote. But the unissued option pool sits inside Company Capitalization, so the Safe converts into 500,000 shares on a 10.5M post-conversion base. Nothing to redline — the definitions do that on their own.`
Sources: `cap-table.md · safe.md §1.3, §1.7`

### § 3 How it runs

An ordered list, numbers `01`–`05` in mono.

- `Ingest` — `Hash every source. raw/ freezes; edit a body and lint fails on drift.`
- `Compile` — `Thirteen pages, each claim carrying a file and a section. No locator, no entry in the memo.`
- `Rank` — `Five clauses by weight: money, then control, then exit, then what is missing, then ambiguity.`
- `Council` — `Four seats, no cross-talk, then an anonymised ranking. The chairman keeps the disagreements.`
- `Deliver, then lint` — `Closing brief first on a pre-close request, then memo, redline, timeline, evidence index, verification log. Lint is the gate before anything ships.`

### § 4 The six deliverables

Six cards. File name in mono, description in body text. The first card is the
brief and must come first.

- `closing_brief.md` — `341 words. What binds today, three edits to push, what to confirm — each edit linked to the redline change that makes it real.`
- `research_memo.md` — `Five issues, each with what the documents say, the assessment, and the action. Council splits kept.`
- `redline.md` — `Ten changes, side letter only. Every strike and insertion footnoted to a reviewer and a source.`
- `fact_timeline.md` — `Dated rows, each cited. Four contested dates marked, including the one nobody can prove.`
- `evidence_index.md` — `One row per source: SHA256, what it supports, what it contradicts.`
- `verification_log.md` — `Eight claims, quoted beside their source. Seven matched. One did not, and it is row 8.`

### § 5 The correction

Callout with a mono flag: `§ 5 · The correction`, heading `What it got wrong`.

Paragraph:
`The memo read opposing counsel's offer as a concession, and wrote that the MFN gap was the cheapest of the three to close. The email says otherwise.`

Pull quote, large:
`“If you want the MFN limited to Safes, say so in one sentence and we'll consider it — I'm not promising we'll agree.”`

Mono attribution: `email-04 · 16 Nov 2026`

Paragraph:
`Row 8 of the verification log records the mismatch, the memo carries a correction log at §7, and the council transcript was left wrong on purpose — an edited transcript would hide the trail. A clean eight-for-eight would have been the less believable artifact.`

Mono links: `verification_log.md row 8 · research_memo.md §7 · council/06-chairman.md`

### § 6 Limits, stated plainly

Three items, label bold, then text.

- `One model, four seats.` — `The reviewers are independent of each other and not independent of the model. Where they disagree, read it; where they agree, it may be the model's prior.`
- `The wiki was not a blank slate.` — `The compile pass formed first views before the council ran. Four disagreements still survived into the memo, but the council was not a rubber stamp either.`
- `Lint checks structure, not sense.` — `It proves a citation points at a heading that exists. It cannot prove the quote supports the claim. That is what the verification log is for — and why its verdict column is still blank.`

### Footer

Mono, small, on a hairline: `Repo` · `SKILL.md` · `MIT` · `Built with AutoClaw · Round 3 · Legal Practice`.

## Publish

- Subdomain `matter-room` → `https://matter-room.lovable.app`
- Public, no password, no workspace-only access
- After publishing, open it in a logged-out browser

## Check before you call it done

1. Six deliverable cards, `closing_brief.md` first, each link opening the right file
   on GitHub.
2. The masthead disclaimer is visible without scrolling.
3. The string "six deliverables" appears; "five deliverables" appears nowhere.
4. No number on the page outside the allowed list.
5. Dark mode: text is readable, hairlines visible, accent still legible.
6. At 375px wide, nothing overflows and the fact strip stacks.
7. Every link returns 200 (the repo links, the six file links, SKILL.md).

---

## Status

Built and published: **https://matter-room.lovable.app** — project
`b44074e7-b469-4456-9602-f98cdbcd42cf`, workspace `Tamazi's Lovable`
(`bacb199e6636426abf61`), published 19 Nov 2026. The build was driven over the
Lovable MCP server; the published page carries the same copy as `docs/index.html`.
