# Matter Room — execution plan (improved)

**Entry:** Built with AutoClaw — Round 3 · Legal Practice (featured track)
**Owner:** Tamaz Sujashvili
**Deadline:** Friday 20 Nov 2026, 23:59 UTC+8 = **19:59 Tbilisi time (UTC+4)**
**Today:** Wednesday 18 Nov 2026 — you have three calendar days, not two.

This replaces the earlier sketch. The old plan named the right repos and the right
award criteria, but it left the build as "write a SKILL.md" and treated AutoClaw as
a side ingest tool. Judges score AutoClaw's role, a complete task→deliverable
workflow, verified results, and a method others can reuse. Those four things are
now the spine of the plan.

---

## 1. What changed from the first draft

| Old plan | This plan |
|---|---|
| Run Karpathy's LLM Council app (Node + OpenRouter) next to AutoClaw | Council runs **inside AutoClaw** as four reviewer personas + a chairman pass. No second stack, no OpenRouter key, one story: "AutoClaw did the work." |
| "Public documents — YC SAFE, NVCA, EDGAR, or your NDA" | One **constructed matter** on a public YC Post-Money SAFE: side letter + term sheet + four emails. A contract alone produces a clause list, not a matter file. |
| Day 1 / Day 2, no buffer | **Wed build · Thu run & verify · Fri post & submit.** Friday is not a work day; it is buffer. |
| Deliverables named, not specified | Exact file tree, frontmatter, citation format, redline format, verification log, X thread copy. |
| "Sources were checked" as a vibe | `lint-matter.py` screenshot + a published `verification_log.md` with eight sampled claims. |
| Skill is a parallel toolchain | AutoClaw Legal Assistant **is** the runtime. The repo is the instruction pack it reads. |

Still cut from scope (do not add these back):

- Clause Graph / `senior-code-mcp` parser rewrite
- SwarmClaim multi-agent orchestration on the critical path
- Karpathy's `llm-council` Node app as a runtime dependency
- Any second track until the Legal entry is posted

---

## 2. The matter (do not skip this)

Judges will not be impressed by "here are the risks in a YC SAFE." They will be
impressed by a matter file that behaves like one: parties, dates, emails that
contradict the paper, a side letter that fights the SAFE's entire-agreement
clause, and a Monday closing.

**Matter: Halden Analytics — pre-close SAFE review.** Entirely fictional. No
client, no leak, no redaction emergency. The privacy rule becomes a strength:
you say so in the post.

| Item | What it is | Where it comes from |
|---|---|---|
| `raw/safe.md` | YC Post-Money SAFE, Valuation Cap, no Discount | Public YC document. Template leg. |
| `raw/side-letter.md` | Investor side letter: pro rata, information rights, MFN | You write it. The live issues live here. |
| `raw/term-sheet.md` | One-page term sheet, slightly older than the SAFE | You write it. Timeline + comparison source. |
| `raw/email-01..04.md` | Founder ↔ investor counsel, 4 short emails | You write them. At least two **contested facts**. |
| Cap table snippet | Pre/post conversion math at the stated cap | You write it. Feeds the Risk reviewer. |

**Live question the memo answers:** the emails promise pro rata and information
rights "of course"; the SAFE is silent and has an entire-agreement clause; the
side letter grants both but conflicts with the SAFE on MFN timing. What does the
founder actually owe, what should be redlined in the side letter before Monday,
and what should stay off the SAFE itself.

Do **not** redline the YC SAFE. You do not redline a market standard. You redline
the side letter and issue-spot the SAFE. That judgment is itself a Quality signal.

Use fictional names, `@halden.example` addresses, and a note in the README that
the matter is constructed. If you would rather use a real matter of your own,
redact it to the same shape — but constructed is faster and safer.

---

## 3. What AutoClaw actually does

The skill is instructions **to AutoClaw**, not a side script. Legal Assistant is
the runtime. You attach the matter folder and say:

> Use Matter Room on this bundle. Produce the wiki, then the council, then the
> memo, redline, timeline, and evidence index.

AutoClaw then:

1. Orients (`SCHEMA.md` + `index.md` + last 20 lines of `log.md`)
2. Ingests each `raw/` file: SHA256, extract, file under the right subdir
3. Compiles L2 pages (parties, obligations, contested facts, comparisons)
4. Risk-ranks clauses into a top-5 list
5. Runs the four-reviewer council on those five
6. Chairman-synthesizes the memo
7. Drafts the side-letter redline
8. Emits timeline + evidence index
9. Runs lint; you fix what it cannot judge

`create-wiki` stays the librarian. `llm-council-skill` contributes the
**protocol** (parallel opinions → anonymized peer review → chairman), not the
Node app. That is the reverse-engineering story, and it is honest.

---

## 4. Repo layout (this is the reusable method)

```
matter-room/
├── SKILL.md                     # the skill AutoClaw reads
├── README.md                    # humans: what it is, 90-sec install, credits
├── templates/
│   ├── SCHEMA.md
│   ├── index.md
│   ├── log.md
│   ├── research_memo.md
│   ├── redline.md
│   ├── fact_timeline.md
│   ├── evidence_index.md
│   └── verification_log.md
├── prompts/
│   ├── risk_rank.md
│   ├── reviewer_risk.md
│   ├── reviewer_missing.md
│   ├── reviewer_consistency.md
│   ├── reviewer_ambiguity.md
│   ├── chairman.md
│   └── verify.md
├── scripts/
│   ├── install.sh               # same pattern as create-wiki
│   └── lint_matter.py           # fork of lint-wiki.py + legal checks
└── examples/
    └── halden-safe/             # the finished matter — this IS the demo URL content
        ├── raw/
        ├── entities/
        ├── concepts/
        ├── comparisons/
        ├── queries/
        ├── deliverables/        # memo, redline, timeline, evidence, verification
        ├── SCHEMA.md
        ├── index.md
        └── log.md
```

Install story, matching `create-wiki`:

```bash
git clone https://github.com/Tamaz-sujashvili/matter-room.git
./matter-room/scripts/install.sh
# then in AutoClaw Legal Assistant:
#   open / attach examples/halden-safe/  (or a new empty matter folder)
#   paste or point at SKILL.md and say "run Matter Room"
```

If AutoClaw has no skill directory you can write to, the README says so plainly:
copy `SKILL.md` + `prompts/` into the chat, attach the folder, run. Reusable does
not require a plugin API.

---

## 5. Schema — keep create-wiki, add four legal fields

Do not invent a new wiki engine. Fork the create-wiki SCHEMA and add:

```yaml
---
type: entity | concept | comparison | query | deliverable
party: halden | meridian | counsel
instrument: safe | side-letter | term-sheet | email
risk: high | medium | low
contested: true | false
confidence: high | medium | low
sources:
  - "[[raw/safe.md#s3-entire-agreement]]"
---
```

**Citation rule (this is "sources were checked"):** every factual claim in an L2
page or deliverable carries `[[raw/<file>.md#<locator>]]`. Locator is a section
anchor, email date, or term-sheet row. A claim without a locator is `confidence:
low` and may not enter the memo.

**Tags (closed list, in SCHEMA.md):**
`obligation`, `right`, `risk-high`, `risk-medium`, `contested`, `uncited`,
`safe`, `side-letter`, `term-sheet`, `email`, `closing-critical`.

**Page thresholds:** no page for a passing defined term. A party, an instrument,
a contested fact, a high-risk clause, or a comparison earns a page. Everything
else lives inside an existing page.

**raw/ is immutable.** Corrections go in L2 pages. SHA256 drift is a lint error,
which is how you show the sources were not quietly edited.

---

## 6. Council protocol (AutoClaw-native)

Top 5 clauses, ranked by AutoClaw before the council, in this order of weight:
money (cap, dilution, dissolution) → control (MFN, information rights) →
exit/termination → missing standard terms → ambiguity.

Four reviewer passes on the **same five clauses**. Each is one AutoClaw turn
with a different prompt file. Reviewers see the clause, the cited raw text, and
nothing about "what the other reviewer said."

| Seat | Prompt file | Looks for |
|---|---|---|
| A — Risk | `reviewer_risk.md` | Dilution, cap math, dissolution preference, uncapped exposure |
| B — Missing | `reviewer_missing.md` | Standard terms the SAFE/side letter omit (pro rata mechanics, notice, amendment) |
| C — Consistency | `reviewer_consistency.md` | Side letter vs SAFE entire-agreement, term sheet vs SAFE, email promises vs paper |
| D — Ambiguity | `reviewer_ambiguity.md` | "Qualifying Securities", conversion mechanics, which document wins on conflict |

**Stage 2 — anonymized review.** Collect the four outputs. Strip seat names.
Label them Response A/B/C/D. One more AutoClaw turn: rank each response on
accuracy and insight, `FINAL RANKING:` last line. Same trick as Karpathy, no
second app.

**Stage 3 — Chairman.** Reads stage-1 outputs + rankings. Writes the memo. Keeps
disagreements in the memo instead of papering over them — a council that always
agrees is a single model with extra steps.

Cost: roughly 4 (stage 1) + 1 (review) + 1 (chairman) + ingest/compile turns.
Well inside a normal AutoClaw session. If a turn is huge, council one clause at
a time rather than all five in one prompt.

---

## 7. Deliverables — definition of done

| File | Done when |
|---|---|
| `deliverables/research_memo.md` | Issue → what the documents say (cited) → assessment → recommended action. Opens with the live question. ≤ 4 pages. Disagreements from the council appear as "Reviewer C flagged / Reviewer A did not." |
| `deliverables/redline.md` | Side letter only. `~~struck~~` **inserted**. Each change has a footnote: which reviewer, which `[[source]]`. No silent rewrites. |
| `deliverables/fact_timeline.md` | Dated rows: term sheet, SAFE, each email, side letter, proposed close. Each row cites its source. Contested dates marked. |
| `deliverables/evidence_index.md` | One row per raw file: path, SHA256, pages/lines, what it supports, what it contradicts. |
| `deliverables/verification_log.md` | Eight claims sampled from the memo. For each: the claim, the cited locator, the quoted source text, and `verified` / `corrected` / `could not verify`. You fill this by hand. |
| Wiki L2 pages | Every page has frontmatter, ≥2 wikilinks, no uncited high-risk claim. |
| `lint_matter.py` output | Zero broken links, zero orphans, zero SHA drift. Screenshot this. |

The wiki is the working file. The five deliverables are what the X post shows.

---

## 8. Lint — fork `lint-wiki.py`, add three legal checks

Keep: broken wikilinks, orphans, index completeness, frontmatter, SHA drift,
oversized pages.

Add:

1. **Uncited high-risk** — any page with `risk: high` and a claim lacking a
   `[[raw/...]]` marker in the same bullet.
2. **Contested without a pair** — `contested: true` but only one source listed.
3. **Deliverable backlinks** — every file in `deliverables/` must be linked from
   `index.md`.

This script is the cheapest "we checked our sources" artifact you will have.
Run it on camera.

---

## 9. Clock (Tbilisi, UTC+4)

Deadline local: **Friday 20 Nov, 19:59**.

### Wednesday 18 Nov — build the pack and the matter

| Block | Do | Done when |
|---|---|---|
| Morning | New repo `matter-room`. Copy `create-wiki` templates. Write `SKILL.md` from this plan §3–§6. | `SKILL.md` exists and a stranger could follow it. |
| Morning | Write the Halden corpus: side letter, term sheet, 4 emails, cap table snippet. Download the YC SAFE. | `examples/halden-safe/raw/` has 7 files. |
| Afternoon | Fork `lint-wiki.py` → `lint_matter.py`, add the three legal checks. | Script runs on an empty matter without crashing. |
| Afternoon | **Rehearsal on a 2-file micro-matter** (SAFE + one email). Ingest + compile only. No council yet. | AutoClaw produced `index.md`, 3–4 L2 pages, one comparison. You know where it fights you. |
| Evening | Fix what the rehearsal broke. Write `prompts/*.md`. | Prompts exist as files, not as ideas. |

Sleep on a working ingest. Do not start the council at midnight.

### Thursday 19 Nov — the real run

| Block | Do | Done when |
|---|---|---|
| Morning | Full Matter Room run on Halden: ingest → compile → risk rank. | Top-5 list written, L2 pages linked. |
| Morning | Council stages 1–3. | Memo draft exists. |
| Afternoon | Redline the side letter. Timeline. Evidence index. | Four of five deliverables in `deliverables/`. |
| Afternoon | `lint_matter.py`. Fix links and orphans. | Clean lint screenshot. |
| Evening | **Hand-verify eight claims.** Write `verification_log.md`. Correct the memo where you were wrong. | Log has eight rows, at least one `corrected` (a clean log looks fake). |
| Evening | Push the repo public. README + example matter. | `github.com/Tamaz-sujashvili/matter-room` loads for a logged-out visitor. |

### Friday 20 Nov — post and submit (buffer, not a work day)

| Block | Do | Done when |
|---|---|---|
| Morning | 90-second screen recording: attach folder → AutoClaw runs → open memo, redline, lint, verification log. No voiceover required if the post narrates. | File < 50 MB or hosted on YouTube/Loom. |
| Morning | Publish the X thread (copy in §11). Follow `@AutoClawAIer` first. | Post is public, has the hashtag and the mention. |
| Midday | Submit the form: account email, follow screenshot, X profile URL, X post URL, track = Legal Practice, demo URL = the GitHub repo. | Form confirmation. |
| Afternoon | Stop. If the form rejected something, you still have hours. | — |

Hard stops: no new features on Friday. No second track. No Clause Graph.

---

## 10. Verification protocol (this is the Outstanding clause)

Outstanding requires verified key results. "I looked at it and it seems right"
does not count.

1. After the memo exists, pick **eight** claims that would embarrass you if wrong.
   Prefer: cap math, entire-agreement vs side letter, MFN timing, one email
   promise, one date, one "the SAFE is silent on X," one conversion mechanic,
   one recommended redline.
2. For each, open the raw file, quote the actual text into
   `verification_log.md`, and mark verified / corrected / could not verify.
3. If `corrected`: fix the memo **and** the L2 page **and** the log. Leave the
   correction visible. A visible correction is a process win, not a fail.
4. Screenshot the log for the X post.

That log is the difference between Quality and Outstanding. It takes 60–90
minutes. Budget it Thursday evening.

---

## 11. X thread (draft — edit voice, not structure)

Post during the campaign window, public, `@AutoClawAIer` + `#BuiltWithAutoClaw`.
Do not put your AutoClaw email in the post.

**1/4 — Context**

> I reverse-engineered two of my agent skills into a legal matter room and ran it on AutoClaw.
>
> The problem: a founder gets a SAFE and a side letter and four emails, and the close is Monday. What does the paper actually owe?
>
> #BuiltWithAutoClaw @AutoClawAIer

**2/4 — Process**

> Matter Room is a skill AutoClaw reads. It ingests the bundle (SHA256 on every source), compiles a matter wiki, ranks the five worst clauses, then runs a 4-reviewer council inside AutoClaw — risk, missing terms, consistency, ambiguity — and a chairman writes the memo.
>
> I built the pattern from my create-wiki and llm-council skills. AutoClaw Legal Assistant is the runtime. I did not run a second model stack.

**3/4 — Result**

> Deliverables AutoClaw produced, which I then verified by hand:
> • research memo (every claim cited to a file + section)
> • redline of the side letter
> • fact timeline
> • evidence index
> • verification log — 8 claims, including one I corrected
>
> Matter is constructed (Halden / Meridian) so nothing real leaked. Repo + example matter: <REPO_URL>

**4/4 — Lessons**

> What I checked myself: the cap math, the entire-agreement fight, and one email promise the SAFE does not grant. AutoClaw missed none of those after the council; it did over-claim one MFN timing point, which the log catches.
>
> Reusable method: clone the repo, attach a matter folder, run the skill. Others should steal the citation rule and the verification log, not just the prompts.

Attach: 3–4 screenshots (wiki graph or index, council disagreement, redline,
verification log) and the 90-second video. First image should be the memo or the
redline, not a logo.

---

## 12. Form checklist (do this once, in order)

1. Follow `@AutoClawAIer` **before** the screenshot.
2. Publish the X post. Confirm it is public in a logged-out browser.
3. Form fields: AutoClaw account email · follow screenshot · X profile URL ·
   X post URL · track **Legal Practice** · product/demo URL.
4. Demo URL: the GitHub repo. If the recording is on YouTube/Loom, put that link
   in the repo README above the fold so one URL carries both.
5. One Legal entry. Do not submit a second Legal post.

---

## 13. Fallbacks (decide in advance, do not improvise Thursday night)

| Failure | Move |
|---|---|
| AutoClaw cannot read a PDF | Save every raw source as markdown yourself on Wednesday. Ingest from `.md`. Nobody scores PDF parsing. |
| Council turns blow the context | Council one clause per turn. Five small turns beat one truncated one. |
| Four reviewers take too long | Drop to three: Risk, Consistency, Ambiguity. Missing-terms folds into Risk. Never drop the chairman. |
| Lint keeps failing at 18:00 Thursday | Screenshot the remaining issues, fix the broken links, ship. A listed known-issue section in the README beats a missed deadline. |
| Verification finds a real error at 20:00 Thursday | Correct it, log it, move on. That is the process working. |
| Repo feels thin as a "product URL" | The `examples/halden-safe/` tree **is** the product. Lead the README with that, not with the SKILL.md. |

If Wednesday's rehearsal never ingests cleanly, the fallback entry is still
Legal Practice, still AutoClaw, but the deliverable is the Halden memo + redline
produced directly in Legal Assistant, with the wiki as a manual artifact and the
skill published as "the method I used." Worse story, same track, same deadline.
Do not switch tracks.

---

## 14. Score preview

| Criterion | Where this plan hits it |
|---|---|
| Legal task type | Contract review + comparison + matter-file organization + drafting (redline) |
| Sources checked | SHA256, locator citations, lint, verification log |
| Named deliverables | Memo, redline, timeline, evidence index — four of the five the rules list |
| Complete workflow | Attach folder → AutoClaw → five files, on video |
| Verified results | `verification_log.md`, including a visible correction |
| Reusable method | Public repo, `SKILL.md`, install script, example matter |
| AutoClaw's role | Runtime, not a logo. Council lives in AutoClaw turns. |
| Originality | Your two skills, reverse-engineered; constructed matter is your drafting |
| Privacy | Fictional matter; nothing to redact in a panic |

The old plan was a good map. This one has addresses, a clock, and a definition
of done. Start with the Halden corpus this morning — the skill is easier to
write once the matter it must handle actually exists.
