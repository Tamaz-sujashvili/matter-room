# NEXT SESSION BRIEFING — read this first

You are finishing **Matter Room** for **Built with AutoClaw — Round 3**, Legal
Practice track.

- Owner: Tamaz Sujashvili
- Deadline: **Friday 20 Nov 2026, 23:59 UTC+8 = 19:59 Tbilisi (UTC+4)**
- This folder is the repo. The demo matter is `examples/halden-safe/`.
- Plan: `matter-room-plan.md`. Do not redesign the architecture.

## State: the build and the run are done

The full Matter Room run has been executed on the Halden matter. Committed and
lint-clean.

- `raw/` — 8 sources, SHA256 stamped, two structural fixes logged with before/after
  hashes
- L2 wiki — 13 pages (4 entities, 5 concepts, 2 comparisons, 2 queries), no broken
  links, no orphans
- `queries/risk-rank-top-5.md` — the five clauses that went to the council
- `council/` — brief, 4 seats, anonymized ranking, chairman; 4 disagreements kept
- `deliverables/` — memo, redline (10 changes), timeline, evidence index,
  verification log (7 quotations match, 1 corrected; verdicts pending your sign-off)
- `python3 scripts/lint_matter.py examples/halden-safe` → **0 errors, 0 warnings**
- `log.md` records every step, including the two places the agent was wrong

## What is left — in order

1. ~~Push the repo public~~ **Done.** `https://github.com/Tamaz-sujashvili/matter-room`
   is live and loads logged out. `origin` is set to HTTPS with the keychain
   credential; the SSH deploy key on this machine belongs to a different repo and
   cannot push here.
2. **Initial the verification log.** Reopen rows 1–8 in
   `deliverables/verification_log.md`, check each quotation, write your verdict and
   initials. Do not initial a row you have not reopened. Row 8 is the correction —
   read it twice.
3. **Record 90 seconds.** Attach `examples/halden-safe/` → run → open the memo, the
   redline, the lint output, the verification log. No voiceover needed.
4. **Post the X thread.** Copy in `matter-room-plan.md` §11. Follow
   `@AutoClawAIer` first, put the hashtag and the mention in post 1, and check the
   post in a logged-out browser. Update 4/4: the correction is the MFN *concession*
   over-claim (email 04), not a timing point.
5. **Submit the form.** Track = Legal Practice. Demo URL =
   `https://github.com/Tamaz-sujashvili/matter-room`.

## Hard rules

- Do not add features. The run is finished; anything new is a Friday risk.
- Do not redline the YC Safe. It is issue-spotted in the memo and that is the point.
- Do not invent a verification verdict. The blank sign-off block is honest and it
  is also the strongest thing in the repo.
- Do not edit `raw/` bodies. Two were fixed before the run and logged; a third edit
  without a log entry breaks the only claim this repo really makes.
- One Legal entry. No second track.

## If something breaks

| Problem | Move |
|---|---|
| Push fails on auth | `git remote -v`, then `git credential-osxkeychain get` — the stored token is `repo`-scoped for `Tamaz-sujashvili` |
| Recorder will not capture the app | Screenshots of memo, redline, lint, log are enough — the post narrates |
| Form rejects the demo URL | Put the recording link at the top of README, resubmit the same URL |
| Late correction found in the memo | Fix it, log it, post it. A visible correction is the process working |
