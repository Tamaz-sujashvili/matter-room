# Matter Room

Turn a contract bundle into a matter file AutoClaw can actually work: evidence
wiki, fact timeline, evidence index, four-reviewer council memo, and a
side-letter redline.

Reverse-engineered from [create-wiki](https://github.com/Tamaz-sujashvili/create-wiki)
and [llm-council-skill](https://github.com/Tamaz-sujashvili/llm-council-skill).
The council runs **inside the agent** — no Node app, no OpenRouter key.

Built for **Built with AutoClaw — Round 3**, Legal Practice track.
The example matter (`examples/halden-safe/`) is **constructed and fictional**.
Company names, people, emails, and amounts are invented so nothing real leaks.

## Why not a chatbot

| Chatbot over a PDF | Matter Room |
|---|---|
| Re-reads the contract every question | Compiles once into a wiki with `[[wikilinks]]` |
| Claims without locators | Every claim cites `[[raw/file.md#section]]` |
| Silent about conflicts | `contested: true` + two sources |
| One model, one opinion | Four reviewer seats, anonymized ranking, chairman keeps disagreements |
| "Trust me" | `verification_log.md` the human fills by hand |
| Redlines the market-standard form | Issue-spots the SAFE, redlines the side letter |

## Quick start

```bash
git clone https://github.com/Tamaz-sujashvili/matter-room.git
cd matter-room
./scripts/install.sh            # prints AutoClaw instructions; or: install.sh claude|cursor|codex|hermes
```

Then in AutoClaw Legal Assistant (or Cursor / Claude Code / Codex / Hermes):

1. Attach or open `examples/halden-safe/` (or a new empty matter folder)
2. Point the agent at `SKILL.md` and say: **"Run Matter Room on this matter."**
3. After the draft deliverables exist, fill `verification_log.md` yourself.

## The five deliverables

| File | What it is |
|---|---|
| `research_memo.md` | Issue → cited facts → assessment → action. Council disagreements kept. |
| `redline.md` | Negotiated document only. Every change footnoted. |
| `fact_timeline.md` | Dated rows, each cited. Contested dates marked. |
| `evidence_index.md` | Every raw file: SHA256, what it supports, what it contradicts. |
| `verification_log.md` | Eight sampled claims, human verdicts. |

Lint is the source-check artifact:

```bash
python3 scripts/lint_matter.py examples/halden-safe
```

## The Halden matter (example)

Pre-close SAFE review. Close is Monday 23 Nov 2026.

- **Halden Analytics, Inc.** (Delaware) — founder company
- **Meridian Ventures I, L.P.** — $400,000 on a YC Post-Money SAFE, $8M cap, no discount
- Side letter adds pro rata, information rights, and MFN
- Four emails contradict the paper on all three adds
- SAFE has an entire-agreement clause

Live question: what does the founder actually owe, and what gets redlined in the
side letter before Monday?

## Credits

- Wiki pattern: Andrej Karpathy's LLM Wiki
- Council protocol: Andrej Karpathy's LLM Council (protocol only; this repo does
  not copy or run that app)
- Skill, prompts, Halden matter: Tamaz Sujashvili, MIT

## License

MIT — see [LICENSE](LICENSE).
