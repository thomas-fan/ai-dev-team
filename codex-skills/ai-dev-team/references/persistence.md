# Persistence

Use repository-local state to control context growth and make work resumable.

## State Layout

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

## Rules

- Read `.ai-team/project-state.md` before planning when it exists.
- Read the active task's `session-state.md` before using old chat history as context.
- Persist every canonical handoff artifact in the current task folder.
- Append owner changes, escalations, and major decisions to `communication-log.md`.
- Rewrite `session-state.md` after each meaningful work session.
- Update `.ai-team/project-state.md` whenever task ownership, status, or pending human gates change.

## Resume Protocol

1. Read `.ai-team/project-state.md`.
2. Identify the active task.
3. Read the active task's `session-state.md`.
4. Read only the files listed in `resume_from`.
5. Continue from `next_action`.

If persisted state conflicts with the repository, log the mismatch in `communication-log.md` and let `Orchestrator` reconcile it.
