#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/codex-skills/ai-dev-team"
TARGET_ROOT="${CODEX_HOME:-$HOME/.codex}/skills"
TARGET_DIR="$TARGET_ROOT/ai-dev-team"
BACKUP_DIR="$TARGET_ROOT/ai-dev-team.backup"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Missing source skill directory: $SOURCE_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_ROOT"

if [[ -e "$BACKUP_DIR" ]]; then
  mv "$BACKUP_DIR" "$BACKUP_DIR.old"
fi

if [[ -e "$TARGET_DIR" ]]; then
  mv "$TARGET_DIR" "$BACKUP_DIR"
fi

cp -R "$SOURCE_DIR" "$TARGET_DIR"

echo "Installed ai-dev-team skill to: $TARGET_DIR"
if [[ -e "$BACKUP_DIR" ]]; then
  echo "Previous version backed up at: $BACKUP_DIR"
fi
