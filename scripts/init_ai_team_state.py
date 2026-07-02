#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = ROOT / "ai-team" / "templates"
PLAYBOOK_PATH = ROOT / "ai-team" / "playbooks" / "persistence-and-recovery.md"

FILES_TO_COPY = {
    "project-state.md": "project-state.md",
}

TASK_FILES_TO_COPY = {
    "communication-log.md": "communication-log.md",
    "session-state.md": "session-state.md",
}


def write_if_missing(source: Path, target: Path) -> None:
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_template_instance(source))


def render_template_instance(source: Path) -> str:
    text = source.read_text()
    marker = "```md\n"
    start = text.find(marker)
    if start == -1:
        return text
    start += len(marker)
    end = text.find("\n```", start)
    if end == -1:
        return text
    return text[start:end].rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize persistent AI team state inside a project.")
    parser.add_argument("project_path", nargs="?", default=".", help="Target project path. Defaults to the current directory.")
    parser.add_argument("--task-id", default="TASK-001", help="Seed task folder name to create. Defaults to TASK-001.")
    args = parser.parse_args()

    project_root = Path(args.project_path).resolve()
    state_root = project_root / ".ai-team"
    tasks_root = state_root / "tasks"
    archive_root = state_root / "archive"
    seed_task_root = tasks_root / args.task_id

    state_root.mkdir(parents=True, exist_ok=True)
    tasks_root.mkdir(parents=True, exist_ok=True)
    archive_root.mkdir(parents=True, exist_ok=True)
    seed_task_root.mkdir(parents=True, exist_ok=True)

    for source_name, target_name in FILES_TO_COPY.items():
        write_if_missing(TEMPLATE_DIR / source_name, state_root / target_name)

    for source_name, target_name in TASK_FILES_TO_COPY.items():
        write_if_missing(TEMPLATE_DIR / source_name, seed_task_root / target_name)

    readme_path = state_root / "README.md"
    if not readme_path.exists():
        readme_path.write_text(
            "# AI Team State\n\n"
            "This directory stores persistent AI team state for the current project.\n\n"
            "Read `project-state.md` first, then the active task's `session-state.md`.\n\n"
            "Reference playbook: "
            f"`{PLAYBOOK_PATH}`\n"
        )

    print(f"Initialized AI team state in: {state_root}")
    print(f"Seed task folder: {seed_task_root}")


if __name__ == "__main__":
    main()
