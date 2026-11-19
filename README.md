# Matter Room

Turn a contract bundle into a matter file an agent can work: evidence wiki, fact
timeline, evidence index, four-reviewer council memo, and a side-letter redline.

Built for **Built with AutoClaw — Round 3**, Legal Practice track. Reverse-engineered
from [create-wiki](https://github.com/Tamaz-sujashvili/create-wiki) and
[llm-council-skill](https://github.com/Tamaz-sujashvili/llm-council-skill). The
council runs **inside the agent** — no Node app, no OpenRouter key, no second model
stack.

**The demo is the example matter: [`examples/halden-safe/`](examples/halden-safe/).**
Open that folder and you see the whole method run end to end — 8 sources, 13 wiki
pages, 4 reviewer seats, 5 deliverables, 0 lint issues.

**Live page:** [tamaz-sujashvili.github.io/matter-room](https://tamaz-sujashvili.github.io/matter-room/)
— the same claims as this README, each one linked to the file that supports it.
Built to `brand.md`, served from `docs/`.

## What the Halden run produced

Halden Analytics (fictional, Delaware) signed a $400k YC Post-Money Safe at an $8M
cap. Six days later counsel sent an unexecuted side letter adding pro rata,
monthly reporting, and an MFN. Close is Monday. Four emails contradict the paper.

The run's findings, all cited to a file and a section:

- **Nothing binds the founder today but the Safe.** The term sheet is non-binding
  and the Safe supersedes every prior understanding. A signed side letter *will*
  bind her, and override the Safe wherever it says it controls — which is why the
  redline, not the memo, is the deliverable that matters.
- **The SAFE's entire-agreement clause is temporal.** §6.2 reaches agreements made
  *before* it, so it kills the term sheet and the 6 November call — not a letter
  signed ten days later. The draft's own §5.2 ("this Side Letter shall control") is
  the real overreach, and it is the first thing to delete.
- **The MFN is the only clause that can move the price.** As drafted it reaches
  convertible notes, so a $250k bridge at a lower cap resets Meridian's cap
  automatically, with no notice and no election.
- **5.00% is not 4.76%.** Purchase Amount ÷ Cap gives the headline; the shares
  actually issued are 500,000 on a 10.5M post-conversion base. The pool sits inside
  Company Capitalization. No redline fixes that — it is what the definitions say.
- **Ten changes to the side letter, none to the Safe.** A market-standard form is
  issue-spotted, not redlined.

And one thing the agent got wrong: it read counsel's MFN offer as a concession when
the text says "we'll consider it — I'm not promising we'll agree". `verification_log.md`
row 8 records the correction, and the memo shows it. Seven of eight sampled claims
held. The sign-off block in that log is **blank on purpose** — the human step is the
part that makes the log worth publishing.

## Why not a chatbot

| Chatbot over a PDF | Matter Room |
|---|---|
| Re-reads the contract every question | Compiles once into a wiki with `[[wikilinks]]` |
| Claims without locators | Every claim cites `[[raw/file.md#section]]` |
| Silently picks a winner in a conflict | `contested: true` + two sources + both readings |
| One model, one opinion | Four seats, anonymized ranking, chairman keeps disagreements |
| "Trust me" | `verification_log.md` a human fills and initials |
| Redlines the market-standard form | Issue-spots the SAFE, redlines the side letter |

## Quick start

```bash
git clone https://github.com/Tamaz-sujashvili/matter-room.git
cd matter-room
./scripts/install.sh            # prints AutoClaw instructions; or claude|cursor|codex|hermes
```

Then in AutoClaw Legal Assistant (or Cursor / Claude Code / Codex / Hermes):

1. Attach or open `examples/halden-safe/` — or a new empty matter folder
2. Point the agent at `SKILL.md` and say: **"Run Matter Room on this matter."**
3. When the draft deliverables exist, fill in `verification_log.md` yourself

## What is in the repo

```
SKILL.md              the instruction pack the agent reads
prompts/              risk rank, four reviewer seats, chairman, verify
templates/            SCHEMA, index, log, and the five deliverable shells
scripts/
  install.sh          copy the pack next to your agent
  lint_matter.py      the source-check artifact (4 legal checks)
  stamp_sources.py    SHA256 of every raw body, into frontmatter
examples/halden-safe/ the finished matter: raw/, entities/, concepts/,
                      comparisons/, queries/, council/, deliverables/
docs/index.html       the public page, served by GitHub Pages
VIDEO_BRIEF.md        what the 90-second recording has to show
brand.md              palette, type and voice rules for the page
```

## Lint is the "sources were checked" artifact

```bash
python3 scripts/lint_matter.py examples/halden-safe
# OK — no issues found
```

Beyond broken links, orphans, index completeness, frontmatter and SHA drift, four
legal checks run:

1. `uncited-high-risk` — a `risk: high` page with no `[[raw/...]]` in the body
2. `contested-unpaired` — `contested: true` with fewer than two sources
3. `deliverable-backlink` — a deliverable missing from `index.md`
4. `bad-anchor` — `[[raw/x.md#anchor]]` where the heading does not exist

Check 4 failed on its first run against this very matter: two anchors the pack
recommended did not exist in the source. That is in `log.md`, with both hashes.

SHA256 is stamped on every raw body. Edit a source after ingest and lint fails —
which is how you show nobody quietly changed the paper.

## The method in one paragraph

Two layers. **L1** is the immutable source set, hashed. **L2** is a wiki the agent
compiles once: parties, instruments, contested facts, comparisons, each page carrying
frontmatter, tags from a closed list, and a locator on every claim. Then a top-5 risk
rank by weight (money → control → exit → missing → ambiguity), four independent
reviewer passes on those five clauses with no cross-talk, an anonymized ranking of
those four outputs, and a chairman who writes the memo and **keeps the
disagreements**. Then the side letter is redlined with every change footnoted to a
reviewer and a source. Nothing of that is novel except the discipline of refusing to
let a claim in without a locator.

## Limits — read these before you trust it

**The four seats are one model.** They are independent of each other — no seat sees
another's output, and the ranking pass sees them anonymised — but they are not
independent of the model that runs them. Where they disagree, the disagreement is
worth reading. Where they agree, it may be the model's prior rather than four
converging judgements. Treat the council as a way to surface objections you would
have missed, not as four experts.

**The compile pass forms views before the council runs.** L2 pages record what each
document says and name the conflicts; three of them also carry a first-pass
assessment. The seats argued exposure and remedy on a separate packet, and four
disagreements survived into the memo — but the wiki was not a blank slate.

**Lint checks structure, not sense.** It proves a citation points at a heading that
exists and that a `risk: high` page quotes something. It cannot tell you the quote
supports the claim. That is what the verification log is for, and why the human
verdict column stays blank until someone reads it.

**Citations are heading slugs.** `[[raw/safe.md#6-miscellaneous]]` resolves in this
repo's linter and in any path-based viewer. Obsidian's own autocomplete writes the
literal heading text instead; both conventions exist and this pack picked one.

## Credits

- Wiki pattern: Andrej Karpathy's LLM Wiki
- Council protocol: Andrej Karpathy's LLM Council — protocol only; this repo does
  not copy or run that app
- Skill, prompts, Halden matter: Tamaz Sujashvili, MIT

## License

MIT — see [LICENSE](LICENSE).
