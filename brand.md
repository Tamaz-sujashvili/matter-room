# Brand — Matter Room

Status: set. Applies to `docs/` (the public demo page).

## Why this direction

The artifact is a legal matter file. The page should read like a drafted
instrument, not like a SaaS landing page: paper, ink, hairline rules, numbered
sections, citations in mono. Nothing decorative that a law firm would not print.

## Palette

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#f7f4ec` | `#14120e` | page background |
| `--card` | `#fffdf7` | `#1b1813` | raised blocks |
| `--ink` | `#191611` | `#f2ece0` | body text, headings |
| `--ink-soft` | `#4f4a41` | `#b6ae9c` | secondary text (AA on paper) |
| `--rule` | `#dcd5c4` | `#332f26` | hairlines, borders |
| `--accent` | `#8f1f16` | `#e5988a` | section numbers, links, marks |

Oxblood, not blue. Blue is what every generated page picks; a stamped document
picks red.

## Typography

- Display and body: system serif stack — Iowan Old Style, Palatino, Georgia.
  Serif throughout is the point; a sans/serif mix would read as a blog.
- Numbers, citations, section marks: system mono.
- Meaure: 68 characters. Headings tight (`-0.02em`), body `1.6` line height.

## Rules

- No gradients, no glass, no drop shadows. One hairline per division.
- Radius 2px maximum.
- Section headings carry `§ n` in mono, accent coloured.
- Every claim on the page links to the file that supports it.
- No invented numbers. If a figure appears, it comes from `raw/` or from lint.

## Voice

Declarative, past tense for what happened, present for what the thing does. No
"revolutionise", no "seamlessly", no exclamation marks. Where the system was
wrong, say so and link to the log.
