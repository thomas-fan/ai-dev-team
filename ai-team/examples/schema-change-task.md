# Example Flow: Feature With Schema Change

## Scenario

Add a customer `lifecycle_stage` field that affects onboarding analytics and internal dashboards.

## Recommended Path

`Orchestrator -> Product Analyst -> Tech Lead -> Feature Engineer -> QA / Test Engineer -> Release / SRE Engineer -> Human approval`

## Why This Uses The Full Path

- user-facing and internal behavior both change
- analytics semantics need clear acceptance criteria
- schema, migration, rollout, and rollback considerations are non-trivial

## Expected Artifacts

- `TaskBrief`: problem statement, priority, workflow path, risk level
- `SpecDoc`: semantics of each stage, non-goals, acceptance criteria, dashboard expectations
- `TechPlan`: schema change, backfill plan, compatibility notes, rollout sequence, observability
- `ImplementationPacket`: migration details, code changes, test coverage, known risks
- `QAVerdict`: migration verification, regression evidence, residual risk summary
- `ReleaseChecklist`: deployment order, rollback path, monitoring watch items, release recommendation
