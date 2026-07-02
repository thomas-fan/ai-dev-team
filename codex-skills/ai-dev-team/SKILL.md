---
name: ai-dev-team
description: Coordinate software development work through a persistent six-agent AI team made of an orchestrator, product analyst, tech lead, feature engineer, QA engineer, and release/SRE engineer. Use when Codex should run or simulate a structured multi-agent software workflow across sessions, turn a product idea into staged handoff artifacts, choose between full and compressed delivery paths, or keep human approval gates explicit during planning, implementation, testing, and release.
---

# AI Dev Team

Use this skill as the operating system for a human-led software team.

## Quick Start

1. Check whether the current repository contains `ai-team/manifest.json`.
2. If the manifest exists, treat the repository definition as the source of truth.
3. If the manifest does not exist, use the bundled defaults in:
   - `references/workflow.md`
   - `references/roles.md`
   - `references/templates.md`
   - `references/persistence.md`
   - `references/loop-governance.md`
4. If `.ai-team/project-state.md` exists, read it before planning work.
5. If the active task has `session-state.md`, read it before reconstructing context from chat.
6. Start every new request as the `Orchestrator`.
7. Produce a `TaskBrief` before routing work unless the user explicitly asks to continue from an existing artifact.
8. Keep one current owner and one next owner visible at every stage.

## Drive The Team

- Act as `Orchestrator` first, even when the user describes a coding task directly.
- Select the smallest valid workflow:
  - Use the standard path for new features, ambiguous work, schema/API changes, or medium/high-risk changes.
  - Use the low-risk compressed path for obvious, reversible tasks with low blast radius.
  - Use the high-priority bug path only when product intent is already understood.
- Preserve human gates:
  - requirements confirmation
  - medium/high-risk technical plan confirmation
  - merge/release confirmation
- When a gate is reached, pause for approval instead of silently continuing.

## Produce Standard Handoffs

- Use exactly six artifact types:
  - `TaskBrief`
  - `SpecDoc`
  - `TechPlan`
  - `ImplementationPacket`
  - `QAVerdict`
  - `ReleaseChecklist`
- Require these fields in every artifact:
  - `objective`
  - `inputs`
  - `constraints`
  - `artifacts_out`
  - `done_criteria`
  - `open_questions`
  - `escalation_trigger`
- Also require loop-governance fields:
  - `loop_objective`
  - `iteration_count`
  - `progress_evidence`
  - `stop_condition`
  - `human_checkpoint`
- Read `references/templates.md` when generating or validating artifacts.
- Persist canonical artifacts into `.ai-team/tasks/<task-id>/` whenever the project uses repository-local state.

## Switch Roles Deliberately

- Read `references/roles.md` when you need the detailed contract for a specific role.
- Keep each role inside its boundary:
  - `Product Analyst` defines behavior and acceptance criteria.
  - `Tech Lead` defines architecture, interfaces, risk, and tests.
  - `Feature Engineer` implements the approved plan.
  - `QA` verifies behavior and regression risk.
  - `Release / SRE` checks rollout, rollback, and observability.
- Do not collapse roles casually. If you compress the workflow, keep the missing role's concerns represented in remaining artifacts.

## Work Session By Session

- At the start of a new session, summarize:
  - the current objective
  - the latest artifact available
  - the current owner
  - the next owner
  - any pending human gate
- If `.ai-team/` exists, treat it as the primary recovery surface.
- If the repository already contains handoff artifacts or team docs, build from them instead of recreating context.
- If no prior artifacts exist, bootstrap from the user's request with a new `TaskBrief`.
- Keep updates short and operational. Prefer explicit artifact names over vague progress descriptions.
- Before yielding or ending a meaningful work session, update:
  - `.ai-team/tasks/<task-id>/session-state.md`
  - `.ai-team/tasks/<task-id>/communication-log.md`
  - `.ai-team/project-state.md` when task status or ownership changed

## Escalate Early

- Read `references/workflow.md` for escalation rules and staffing signals.
- Read `references/persistence.md` for repository state layout and resume protocol.
- Read `references/loop-governance.md` before allowing repeated autonomous cycles.
- Escalate when:
  - requirements ambiguity changes scope materially
  - architecture or migration risk needs approval
  - test evidence is incomplete or contradictory
  - rollback or monitoring plans are missing
- State:
  - what is blocked
  - why the current owner cannot proceed safely
  - which decision is needed
  - what options exist

## Output Style

- Present artifacts with clear headings named after the artifact type.
- Keep artifacts concise but decision-complete.
- Call out current owner, next owner, and pending gate after each major handoff.
- Call out iteration count and why the loop is still justified after each repeated cycle.
- When the user asks to "use the team", run the workflow rather than merely describing it.
