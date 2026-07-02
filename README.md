# AI Software Development Team v1

This repository contains an opinionated, reusable operating system for a six-agent AI software development team.

## What is included

- `ai-team/manifest.json`: machine-readable source of truth for roles, handoffs, workflow, gates, and staffing signals
- `ai-team/roles/`: role contracts and default prompt guidance for each agent
- `ai-team/templates/`: six standardized handoff objects used between agents
- `ai-team/playbooks/`: workflow, escalation, and staffing policies
- `ai-team/playbooks/persistence-and-recovery.md`: behavioral norms for persisted state, recovery, and context control
- `ai-team/playbooks/loop-governance.md`: human-supervised loop control, stop conditions, and budget proxies
- `ai-team/examples/`: sample task flows for common Web/SaaS work
- `scripts/validate_ai_team.py`: local validator for the team manifest and file structure
- `scripts/init_ai_team_state.py`: scaffold a project-local persistent state directory

## Operating model

- Team shape: `1 orchestrator + 5 specialist agents`
- Primary mode: `single human operator, async handoffs, single repo`
- Human decision gates:
  - requirement confirmation
  - medium/high-risk technical plan confirmation
  - merge/release confirmation

## Quick start

1. Start with [`TaskBrief`](./ai-team/templates/task-brief.md) for any new request.
2. Route the task using the standard flow in [`operating-model.md`](./ai-team/playbooks/operating-model.md).
3. Require every handoff to use one of the six templates in `ai-team/templates/`.
4. Escalate using [`escalation-rules.md`](./ai-team/playbooks/escalation-rules.md) when the current owner hits a gate.
5. Review staffing pressure using [`staffing-signals.md`](./ai-team/playbooks/staffing-signals.md) before adding new agent roles.
6. Initialize project state with `python3 scripts/init_ai_team_state.py /path/to/project`.

## Persistence And Recovery

To keep work resumable across sessions, store team state inside each project:

```text
.ai-team/
  project-state.md
  tasks/
    TASK-001/
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

Behavioral rules:

- `Orchestrator` owns `.ai-team/project-state.md`
- every task gets its own folder under `.ai-team/tasks/`
- every owner change appends to `communication-log.md`
- every meaningful session rewrites `session-state.md`
- every canonical artifact is persisted into the task folder before handoff

## Loop Governance

This team now uses a bounded `loop engineering` model rather than open-ended autonomy.

Core rules:

- every repeated cycle must name a `loop_objective`
- every artifact records `iteration_count`, `progress_evidence`, `stop_condition`, and `human_checkpoint`
- same-owner loops stop after `3` iterations without new evidence
- QA and implementation cannot bounce more than `2` times without human review
- repeated blockers, unstable scope, or missing `next_action` force a human pause

This keeps the team useful for long-horizon work without letting it drift into dead loops or uncontrolled token burn.

Bootstrap a project with:

```bash
python3 scripts/init_ai_team_state.py /path/to/project --task-id TASK-001
```

Recovery flow:

1. Read `.ai-team/project-state.md`
2. Open the active task's `session-state.md`
3. Read only the files listed in `resume_from`
4. Continue from `next_action`

## Validation

Run:

```bash
python3 scripts/validate_ai_team.py
```

The validator confirms the manifest has the required roles, handoff objects, fields, workflow, and referenced files.

## Use In Every Session

To make the team available in future Codex sessions, install the bundled global skill:

```bash
bash scripts/install_ai_dev_team_skill.sh
```

This copies `codex-skills/ai-dev-team` into `~/.codex/skills/ai-dev-team` or `$CODEX_HOME/skills/ai-dev-team`.

After installation, start a new session and invoke it with a prompt like:

```text
Use $ai-dev-team to build this feature through the right agent workflow.
```

The skill will:

- use the repository's `ai-team/manifest.json` when present
- fall back to bundled default team rules when no repo-local manifest exists
- read and write `.ai-team/` persistent state when present
- start as `Orchestrator`
- produce standard handoff artifacts and preserve human approval gates
