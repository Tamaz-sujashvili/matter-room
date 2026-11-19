# Video brief — the 90-second demo

**Owner:** Tamaz. **Recorded with:** Recordly. **Produced by:** a separate AutoClaw
agent working from a fresh clone of this repo.

The video is the only artifact a judge may watch without reading anything. It has
to prove the workflow ran. It does not have to be narrated, and it must not be
pretty at the expense of being true.

## Hard requirements

1. **A real run, from a fresh clone.** No mock-ups, no slides, no edited screenshots
   pretending to be a screen recording.
2. **Under 90 seconds.** Longer gets skipped.
3. **1280×720 or larger.** Cursor visible.
4. **No credentials on screen.** No terminal history, no keychain prompts, no browser
   tabs with a signed-in account other than the repo and the live page.
5. **Do not show `Built with AutoClaw — Round 3：Official Rules.md`.** It is not part
   of this project and is intentionally untracked.
6. **Under 50 MB** if attached directly, otherwise host it on YouTube or Loom.

## The run the agent should execute on camera

```bash
git clone https://github.com/Tamaz-sujashvili/matter-room.git
cd matter-room
python3 scripts/lint_matter.py examples/halden-safe      # OK — no issues found
python3 scripts/stamp_sources.py examples/halden-safe --check   # 8 sources, 0 needing attention
```

That is the whole "sources were checked" claim in two commands, and both are
reproducible by a judge.

## Shot list

| Time | On screen | Why it is there |
|---|---|---|
| 0:00–0:12 | The repo landing page, then `examples/halden-safe/` | A bundle of documents, not a chat window |
| 0:12–0:25 | `index.md` | 8 sources, 13 cited pages, the council, the five deliverables |
| 0:25–0:38 | `council/06-chairman.md`, section "Disagreements carried into the memo" | The council is not a rubber stamp |
| 0:38–0:52 | `deliverables/research_memo.md` §3.1 and §3.2 | The legal reading, with citations on every claim |
| 0:52–1:05 | `deliverables/redline.md` change 1 | Struck text, inserted text, footnote naming reviewer C and the source |
| 1:05–1:20 | Terminal: lint, then `stamp_sources.py --check` | Two commands, reproducible |
| 1:20–1:30 | `verification_log.md` row 8 | The correction. End on it, not on a logo |

## After recording

1. Upload to YouTube (unlisted) or Loom.
2. Paste the URL into `docs/index.html`, in the `VIDEO_URL` constant near the bottom.
   The "Watch the 90 seconds" button appears only when that string is non-empty.
3. Push. Wait a minute. Open the live page logged out and confirm the button plays.
4. Put the same URL in the X post only if you are posting the video with it — the
   page already carries it.

## What not to claim in the video or the post

- Do not call the results "verified". Eight claims were sampled, seven quotations
  matched, one was corrected, and the human verdict column is still blank.
- Do not describe the matter as real. Halden Analytics and Meridian Ventures do not
  exist, and the page says so in the footer.
- Do not describe the council as four independent experts. It is one model in four
  seats, and the README says so under Limits.
