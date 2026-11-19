# Video brief — the 85-second demo

**Owner:** Tamaz. **Recorded with:** Recordly. **Produced by:** a separate AutoClaw
agent working from a fresh clone of this repo.

The video is the only artifact a judge may watch without reading anything. It has to
show one recommendation travelling from the closing brief to the source email to the
redline. It does not have to be narrated, and it must not be pretty at the expense of
being true.

## Hard requirements

1. **A real run, from a fresh clone.** No mock-ups, no slides, no edited screenshots
   pretending to be a screen recording. One run, one take.
2. **Under 90 seconds.** Longer gets skipped.
3. **1080p, 30 fps.** Cursor visible, text readable at export size.
4. **Under 50 MB** as `matter-room-demo.mp4`.
5. **No credentials on screen.** No terminal history, no keychain prompts, no
   signed-in browser account.
6. **Do not show `Built with AutoClaw — Round 3：Official Rules.md`.** It is not part
   of this project and is intentionally untracked.
7. **Keep the export local.** Do not upload it.

## Set up the matter, then record

The shipped `examples/halden-safe/` already contains a memo, a council record and a
redline. If you record that folder you are recording a finished artifact, not the
workflow. Build a clean matter first, and record the run in it.

```bash
git clone https://github.com/Tamaz-sujashvili/matter-room.git
cd matter-room
MATTER="$(mktemp -d)/halden-close"
mkdir -p "$MATTER/raw" "$MATTER/deliverables"
cp templates/SCHEMA.md templates/index.md templates/log.md "$MATTER/"
cp examples/halden-safe/raw/*.md "$MATTER/raw/"
ls "$MATTER/raw" | wc -l      # 8
```

Only the eight fictional sources go in. No memo, no council page, no redline: the
next step generates those from the sources.

Open `$MATTER` in AutoClaw Legal Assistant and submit this prompt:

> We represent Halden. The wire is Monday. Compare the signed SAFE and Meridian’s
> draft side letter with the term sheet and emails. What binds us today, and what are
> the three changes I should push before signing? Give me a one-page brief for the
> partner and mark up the side letter. Quote the email for anything you say we
> agreed to.

The skill routes a pre-close request to `deliverables/closing_brief.md` first. If the
run opens with a memo, the routing is broken — stop and fix it, do not record around
it.

## Check the run before you record anything else

```bash
python3 scripts/lint_matter.py "$MATTER"                     # OK — no issues found
python3 scripts/stamp_sources.py "$MATTER" --check           # 8 sources, 0 needing attention
```

Lint enforces the brief's structure: 350-word cap, the three sections, a declared
count that matches, a link to a numbered redline change, and at least one evidence
label. Hashes prove the sources were not edited.

Four things lint cannot judge. Read them yourself:

1. The MFN email stays a **proposal**. The text is "we’ll consider it — I’m not
   promising we’ll agree", and no summary may upgrade it.
2. The founder’s silence on pro rata stays **unresolved**. She answered information
   rights and MFN on 14 November and said nothing about pro rata.
3. The term sheet’s confidentiality and expense carve-outs are named before the
   brief concludes what binds.
4. The markup changes the side letter and nothing else. The Safe is executed and
   market standard; it is issue-spotted, never redlined.

If a check fails, fix the skill and rerun from a clean matter. Do not fix the brief
by hand and film the hand-fixed file.

## Record

Start Recordly directly, with the Codex computer-use overlay closed. Select AutoClaw
only, record a five-second test, and play it back at export size. The test passes when
the frame holds only the AutoClaw window and the text is readable. If Recordly
captures Codex, or shrinks AutoClaw to a preview, fix the capture setup before
filming.

| Time | On screen | Why it is there |
|---|---|---|
| 0:00–0:12 | `$MATTER` in Finder or an editor, eight source files, then the prompt typed into AutoClaw | A bundle of documents, not a chat window |
| 0:12–0:22 | Ingest running; trim the wait, keep enough to show work happening | The run is real |
| 0:22–0:40 | `deliverables/closing_brief.md`, "What binds today", then edit 1 | The answer, and the evidence under it |
| 0:40–0:55 | `raw/email-04.md`, "we’ll consider it — I’m not promising we’ll agree" | The label is earned by the sentence |
| 0:55–1:15 | `deliverables/redline.md`, change 1: struck text, inserted text, footnote | The recommendation became a redline |
| 1:15–1:25 | `deliverables/verification_log.md`, rows 4–6, verdict column `pending` | The claim sits beside its source, and the human has not signed |

Zoom on the quotation and on the struck and inserted text. A viewer must be able to
read them without pausing on a 1080p screen.

The terminal is not in the shot list. Run both commands anyway and report their
output: the checks are integrity evidence in the reply, and a twelve-second terminal
shot costs the brief the space it needs.

## Export and report

Recordly trims and zooms on one take. Export `matter-room-demo.mp4` at 1080p, 30 fps,
under 90 seconds and 50 MB. Review the exported file end to end — not the timeline,
the file — then report:

- the local path
- verified specs (`ffprobe`: resolution, frame rate, duration, size)
- the actual shot timings
- the two command results, verbatim

## What not to claim in the video or the post

- Do not call the results "verified". Six claims are sampled, quotations are compared,
  and the human verdict column is blank. That is the point.
- Do not describe the matter as real. Halden Analytics and Meridian Ventures do not
  exist, and the page footer says so.
- Do not show or imply a council. This run is a pre-close pass; the four seats belong
  to the full review in `examples/halden-safe/`, which is one model in four seats and
  says so under Limits.
- Do not present the three edits as accepted. Two are requests; one is a trade.
