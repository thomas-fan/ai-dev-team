# Workflow

## Standard Path

`Orchestrator -> Product Analyst -> Tech Lead -> Feature Engineer -> QA -> Release / SRE -> Human approval`

Use for:

- new features
- ambiguous requirements
- schema or API changes
- medium/high-risk work

## Low-Risk Compressed Path

`Orchestrator -> Tech Lead -> Feature Engineer -> QA -> Release / SRE -> Human approval`

Use for:

- obvious CRUD-style work
- reversible changes
- low blast-radius tasks

## High-Priority Bug Path

`Tech Lead -> Feature Engineer -> QA -> Release / SRE -> Human approval`

Use for:

- already-understood bugs
- work where product intent is already settled
- urgent fixes where discovery cost should stay low

## Human Gates

- `requirements_confirmation`
- `technical_plan_confirmation`
- `merge_release_confirmation`

Pause and ask for approval when a gate is reached.

## Escalation Rules

Escalate when:

- requirements ambiguity changes scope materially
- architecture, compatibility, migration, or reliability risk needs approval
- implementation reveals a risky deviation from plan
- test evidence is incomplete or contradictory
- rollback or monitoring plans are missing

Include:

- blocked issue
- reason work cannot proceed safely
- decision needed
- viable options

## Staffing Signals

Add specialists only when a repeated bottleneck justifies the extra coordination overhead.

- Add `UI/UX specialist` when interaction ambiguity repeatedly delays specs.
- Add `security specialist` when security review repeatedly blocks release.
- Add `data/ai specialist` when roadmap work becomes model- or data-heavy.
- Add `independent reviewer` when tech lead review queue becomes the bottleneck.
