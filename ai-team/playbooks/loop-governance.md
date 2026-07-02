# Loop Governance

This playbook adapts the team's operating model to a loop-engineering style of work while preserving hard human control over cost and runaway autonomy.

## Design Principles

The policy here is informed by recent public discussion of `loop engineering` as a shift from one-off prompting toward repeatable agent loops, plus current research emphasizing artifact engineering, budget engineering, and human-in-the-loop supervision for reliable agents.

Design consequences for this team:

- every loop must have a defined objective
- every loop must leave durable artifacts on disk
- every loop must have explicit stop conditions
- every loop must expose cheap human intervention points

## What Counts As A Loop

A loop is any bounded repeat-until-done execution pattern where one or more agents continue planning, acting, validating, or re-planning without fresh user prompting at every step.

Examples:

- implement -> test -> fix -> retest
- spec clarification -> revise spec -> approval check
- review -> revise -> review
- release hardening -> verify rollback -> update checklist

## Required Loop Fields

Every canonical artifact must record:

- `loop_objective`
- `iteration_count`
- `progress_evidence`
- `stop_condition`
- `human_checkpoint`

These fields make loops auditable and resumable across sessions.

## Hard Limits

- maximum same-owner iterations: `3`
- maximum cross-role rework cycles: `2`
- maximum failed validation cycles: `2`
- maximum open questions before pause: `5`

These are defaults. A human may explicitly loosen them for an unusual task, but the override must be written into `communication-log.md` and `session-state.md`.

## Mandatory Human Pause Triggers

Pause and ask for human direction when any of these occur:

- the same blocker appears twice
- the same owner iterates three times without new evidence
- QA and implementation bounce twice without narrowing scope
- architecture or schema changes appear after implementation already started
- `session-state.md` cannot name a concrete `next_action`
- cost risk is rising faster than uncertainty is shrinking

## Progress Tests

An iteration counts as real progress only if at least one is true:

- a canonical artifact became more complete
- a failing test was converted into a passing test
- the defect surface got smaller
- an open question was resolved
- rollout or rollback uncertainty was reduced

If none of these are true, treat the iteration as churn.

## Human Supervision Pattern

Use bounded autonomy rather than open-ended autonomy.

- let the team operate inside a small loop budget
- force a pause at meaningful checkpoints
- ask for decisions only when there is a real branch, risk increase, or budget concern

Recommended human checkpoints:

- after `SpecDoc` for medium/high-risk work
- after `TechPlan` for medium/high-risk work
- after two implementation or QA iterations
- before merge or release

## Token And Cost Control

Since direct token accounting may not always be available inside the workflow, use these operational proxies:

- minimize parallel specialists unless a second opinion is truly valuable
- prefer repository state and concise artifacts over re-explaining history in chat
- stop re-reading the whole task history once `session-state.md` is trustworthy
- do not spawn another specialist only to restate the same unresolved issue
- escalate sooner when repeated work is producing explanation, not evidence

## Role-Specific Loop Rules

- `Orchestrator`: pauses loops when churn is visible
- `Product Analyst`: stops clarification after repeated ambiguity without new facts
- `Tech Lead`: stops redesign after repeated plan instability
- `Feature Engineer`: stops editing after repeated no-progress test cycles
- `QA`: stops bounce loops when defect scope is not shrinking
- `Release / SRE`: stops release polishing when operational uncertainty is not decreasing

## Resume And Audit

At the end of each meaningful session:

- update `session-state.md`
- append the loop decision to `communication-log.md`
- update `project-state.md` if ownership, status, or gates changed

That persisted trail is the authoritative recovery surface for the next session.
