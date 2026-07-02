# Example Flow: Small CRUD Feature

## Scenario

Add a status filter to an admin customer list page.

## Recommended Path

`Orchestrator -> Tech Lead -> Feature Engineer -> QA / Test Engineer -> Release / SRE Engineer -> Human approval`

## Why This Uses The Compressed Path

- product intent is obvious
- no new business workflow is being invented
- the blast radius is limited and reversible

## Expected Artifacts

- `TaskBrief`: scope, deadline, workflow path, risk level
- `TechPlan`: UI/API touchpoints, query parameter changes, test plan
- `ImplementationPacket`: code changes, tests, manual verification steps
- `QAVerdict`: filter behavior, empty state, regression checks
- `ReleaseChecklist`: config impact should likely be none, rollback should be straightforward
