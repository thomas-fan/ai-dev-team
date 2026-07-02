#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_ROOT="${CODEX_HOME:-$HOME/.codex}/skills"
TARGET_DIR="$TARGET_ROOT/ai-dev-team"

if [[ -d "$TARGET_DIR" ]]; then
  echo "Updating existing ai-dev-team skill at: $TARGET_DIR"
else
  echo "ai-dev-team is not installed yet. Performing first install."
fi

bash "$ROOT_DIR/scripts/install_ai_dev_team_skill.sh"

echo "Restart Codex to pick up the updated skill."
