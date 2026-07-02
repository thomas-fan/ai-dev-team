# Operating Model

## Standard Path

`Orchestrator -> Product Analyst -> Tech Lead -> Feature Engineer -> QA / Test Engineer -> Release / SRE Engineer -> Human approval`

Use the standard path when the request is a new feature, carries medium/high risk, changes user-facing behavior, or introduces non-obvious rollout concerns.

## Exception Paths

### Low-Risk Small Task

`Orchestrator -> Tech Lead -> Feature Engineer -> QA / Test Engineer -> Release / SRE Engineer -> Human approval`

Use this when:

- scope is obvious from the request
- no meaningful product ambiguity exists
- the change is reversible and low blast radius

### High-Priority Bug

`Tech Lead -> Feature Engineer -> QA / Test Engineer -> Release / SRE Engineer -> Human approval`

Use this when:

- the bug is already understood
- product intent is already known
- speed matters more than full discovery

## Human Gates

- `requirements_confirmation`: approve the `SpecDoc` before medium/high-risk implementation
- `technical_plan_confirmation`: approve the `TechPlan` for medium/high-risk work, especially API/schema/architecture changes
- `merge_release_confirmation`: approve merge or release after `QAVerdict` and `ReleaseChecklist`

## Ownership Rules

- one current owner at a time
- no ownership transfer without a handoff object
- the owner who discovers ambiguity must either resolve it or escalate it
- skipped roles do not remove quality obligations; their concerns must still be represented in the remaining artifacts

## Loop Controls

- every active loop must have a `loop_objective` and `stop_condition`
- no role may exceed three same-owner iterations without new evidence
- QA and implementation may not bounce more than twice without human review
- if progress cannot be summarized as evidence in `session-state.md`, pause the loop
- see [`loop-governance.md`](./loop-governance.md) for hard limits and intervention triggers
