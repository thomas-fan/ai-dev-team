#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "ai-team" / "manifest.json"

REQUIRED_ROLE_IDS = {
    "orchestrator",
    "product-analyst",
    "tech-lead",
    "feature-engineer",
    "qa-test-engineer",
    "release-sre",
}

REQUIRED_HANDOFF_IDS = {
    "TaskBrief",
    "SpecDoc",
    "TechPlan",
    "ImplementationPacket",
    "QAVerdict",
    "ReleaseChecklist",
}

REQUIRED_HANDOFF_FIELDS = [
    "objective",
    "inputs",
    "constraints",
    "artifacts_out",
    "done_criteria",
    "open_questions",
    "escalation_trigger",
]

EXPECTED_STATE_ROOT = ".ai-team"
REQUIRED_OPERATIONAL_ARTIFACTS = {
    "project-state.md",
    "session-state.md",
    "communication-log.md",
}
REQUIRED_LOOP_FIELDS = {
    "loop_objective",
    "iteration_count",
    "progress_evidence",
    "stop_condition",
    "human_checkpoint",
}

EXPECTED_STANDARD_WORKFLOW = [
    "orchestrator",
    "product-analyst",
    "tech-lead",
    "feature-engineer",
    "qa-test-engineer",
    "release-sre",
    "human",
]

EXPECTED_GATES = {
    "requirements_confirmation",
    "technical_plan_confirmation",
    "merge_release_confirmation",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def ensure(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_manifest() -> dict:
    ensure(MANIFEST_PATH.exists(), f"Missing manifest: {MANIFEST_PATH}")
    try:
        return json.loads(MANIFEST_PATH.read_text())
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in manifest: {exc}")


def ensure_files_exist(paths: list[str], label: str) -> None:
    for relative in paths:
        path = ROOT / relative
        ensure(path.exists(), f"Missing {label} file: {relative}")


def validate_roles(manifest: dict) -> None:
    roles = manifest.get("roles", [])
    role_ids = {role.get("id") for role in roles}
    ensure(role_ids == REQUIRED_ROLE_IDS, f"Role IDs mismatch: {sorted(role_ids)}")

    for role in roles:
        for key in ("id", "title", "file", "consumes", "produces", "human_gate"):
            ensure(key in role, f"Role {role.get('id')} missing key: {key}")
        ensure_files_exist([role["file"]], "role")


def validate_handoffs(manifest: dict) -> None:
    handoffs = manifest.get("handoff_objects", [])
    handoff_ids = {handoff.get("id") for handoff in handoffs}
    ensure(handoff_ids == REQUIRED_HANDOFF_IDS, f"Handoff IDs mismatch: {sorted(handoff_ids)}")
    ensure(
        manifest.get("required_handoff_fields") == REQUIRED_HANDOFF_FIELDS,
        "Required handoff fields list does not match expected baseline",
    )

    for handoff in handoffs:
        for key in ("id", "template"):
            ensure(key in handoff, f"Handoff missing key: {key}")
        ensure_files_exist([handoff["template"]], "handoff template")


def validate_workflow(manifest: dict) -> None:
    workflow = manifest.get("workflow", {})
    ensure(workflow.get("standard") == EXPECTED_STANDARD_WORKFLOW, "Standard workflow does not match expected path")
    ensure(set(workflow.get("human_gates", [])) == EXPECTED_GATES, "Human gates mismatch")

    exceptions = {item.get("name"): item.get("path") for item in workflow.get("exceptions", [])}
    ensure("low-risk-small-task" in exceptions, "Missing low-risk-small-task exception path")
    ensure("high-priority-bug" in exceptions, "Missing high-priority-bug exception path")


def validate_persistence(manifest: dict) -> None:
    persistence = manifest.get("persistence")
    ensure(isinstance(persistence, dict), "Missing persistence configuration")
    ensure(persistence.get("state_root") == EXPECTED_STATE_ROOT, "Unexpected persistence state_root")
    ensure("templates" in persistence, "Persistence configuration missing templates")
    ensure(
        set(persistence.get("operational_artifacts", [])) == REQUIRED_OPERATIONAL_ARTIFACTS,
        "Operational artifacts mismatch",
    )
    templates = persistence.get("templates", {})
    for key in ("project_state", "session_state", "communication_log"):
        ensure(key in templates, f"Persistence templates missing key: {key}")
    ensure_files_exist(list(templates.values()), "persistence template")


def validate_loop_control(manifest: dict) -> None:
    loop_control = manifest.get("loop_control")
    ensure(isinstance(loop_control, dict), "Missing loop_control configuration")
    for key in (
        "playbook",
        "human_supervision_model",
        "max_same_owner_iterations",
        "max_cross_role_rework_cycles",
        "max_failed_validation_cycles",
        "max_open_questions_before_pause",
        "mandatory_pause_triggers",
        "required_fields",
    ):
        ensure(key in loop_control, f"loop_control missing key: {key}")
    ensure_files_exist([loop_control["playbook"]], "loop-governance playbook")
    ensure(set(loop_control.get("required_fields", [])) == REQUIRED_LOOP_FIELDS, "Loop control required fields mismatch")


def validate_references(manifest: dict) -> None:
    ensure_files_exist(manifest.get("playbooks", []), "playbook")
    ensure_files_exist(manifest.get("examples", []), "example")
    staffing_signals = manifest.get("staffing_signals", [])
    ensure(len(staffing_signals) >= 4, "Expected at least four staffing signals")
    for signal in staffing_signals:
        ensure("signal" in signal and "add_role" in signal, "Invalid staffing signal entry")


def main() -> None:
    manifest = load_manifest()
    validate_roles(manifest)
    validate_handoffs(manifest)
    validate_workflow(manifest)
    validate_persistence(manifest)
    validate_loop_control(manifest)
    validate_references(manifest)
    print("AI team manifest validation passed.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
