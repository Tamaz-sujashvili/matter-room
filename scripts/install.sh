#!/usr/bin/env bash
# Install Matter Room skill instructions next to the agent that will run them.
# Usage: ./scripts/install.sh [autoclaw|claude|cursor|codex|hermes|all|print]
# Default target: print (AutoClaw has no stable skill dir we can assume).

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

install_dir() {
  local dest="$1"
  mkdir -p "$dest"
  cp -R "$SRC/SKILL.md" "$SRC/prompts" "$SRC/templates" "$SRC/scripts" "$dest/"
  echo "Installed Matter Room -> $dest"
}

print_autoclaw() {
  cat <<EOF
AutoClaw Legal Assistant has no plugin API we can assume.

1. Open AutoClaw desktop app → Legal Assistant
2. Attach or open a matter folder (examples/halden-safe, or a new empty folder)
3. Paste SKILL.md into the chat, or add it as a project instruction if your
   build supports one, and say:

     Run Matter Room on this matter. Follow SKILL.md. Do not skip ingest.

4. After draft deliverables exist, fill verification_log.md yourself.

Reusable does not require a plugin API. The repo is the method.
EOF
}

case "${1:-print}" in
  print|autoclaw)
    print_autoclaw
    ;;
  claude)
    install_dir "$HOME/.claude/skills/matter-room"
    ;;
  cursor)
    install_dir "$HOME/.cursor/skills/matter-room"
    ;;
  codex)
    install_dir "$HOME/.codex/skills/matter-room"
    ;;
  hermes)
    install_dir "$HOME/.hermes/skills/legal/matter-room"
    ;;
  all)
    print_autoclaw
    install_dir "$HOME/.claude/skills/matter-room"
    install_dir "$HOME/.cursor/skills/matter-room"
    install_dir "$HOME/.codex/skills/matter-room"
    install_dir "$HOME/.hermes/skills/legal/matter-room"
    ;;
  *)
    echo "Usage: $0 [autoclaw|claude|cursor|codex|hermes|all|print]" >&2
    exit 2
    ;;
esac
