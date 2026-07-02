# Persistence And Recovery

This playbook defines how the team persists communication, design artifacts, and resumable state inside each project repository.

## Goals

- keep chat context small by moving durable state to files
- make handoffs inspectable without replaying the full conversation
- recover work after interruptions, crashes, or model/session resets

## Project State Layout

Persist team state inside a project-local `.ai-team/` directory.

```text
.ai-team/
  project-state.md
  tasks/
    TASK-ID/
      task-brief.md
      spec-doc.md
      tech-plan.md
      implementation-packet.md
      qa-verdict.md
      release-checklist.md
      communication-log.md
      session-state.md
  archive/
```

## Required Operational Files

### `project-state.md`

Repository-level index of all active, blocked, pending, and archived work.

It must answer:

- what tasks are active right now
- who owns each task
- what the next required artifact is
- whether a human gate is pending

### `communication-log.md`

Append-only log for agent-to-agent coordination that is too transient for the canonical handoff artifacts but too important to lose.

Record:

- major decisions
- clarifications
- escalations
- blockers
- deviations from plan

Do not use it as a substitute for `SpecDoc`, `TechPlan`, or other canonical artifacts.

### `session-state.md`

Single-file recovery checkpoint for the current task. Rewrite it at the end of every meaningful session or owner change.

It must answer:

- current owner
- next owner
- latest completed artifact
- exact next action
- blocker status
- files to read first when resuming

## Behavioral Norms

- Before starting work, read `.ai-team/project-state.md` and the current task's `session-state.md` if they exist.
- Before handing work to another role, persist the canonical artifact for that stage into the task folder.
- After every owner change, append a short entry to `communication-log.md`.
- Before ending a session, rewrite `session-state.md` with the newest recovery checkpoint.
- If the repo state changes materially, update `project-state.md` in the same session.
- If the task is complete or abandoned, mark it in `project-state.md` and move the task folder to `archive/` only after human approval.

## Artifact Ownership

- `Orchestrator` owns `project-state.md` and creates task folders.
- Each specialist owns the canonical artifact for their stage.
- The current owner is responsible for updating `session-state.md` before yielding.
- Anyone escalating an issue must record it in `communication-log.md`.

## Resume Protocol

When resuming after interruption:

1. Read `.ai-team/project-state.md`.
2. Identify the active task and current owner.
3. Read that task's `session-state.md`.
4. Read only the files listed in `resume_from`.
5. Continue from `next_action` rather than reconstructing the entire chat.
6. If persisted state conflicts with the repo, log the mismatch in `communication-log.md` and let `Orchestrator` reconcile it.

## Context Control Rules

- Keep canonical decisions in artifacts, not chat prose.
- Summaries in chat should reference files, not restate them fully.
- Prefer updating one persisted document over re-explaining history in every session.
- Treat `session-state.md` as the minimum recovery surface and `project-state.md` as the minimum portfolio surface.
