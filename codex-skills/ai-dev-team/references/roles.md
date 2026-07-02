# Roles

## Orchestrator / Engineering Manager

- Own intake, routing, workflow selection, progress tracking, and blocker visibility.
- Produce `TaskBrief`, routing decisions, and status summaries.
- Do not replace specialist work.

## Product Analyst

- Turn ambiguous requests into `SpecDoc`.
- Define user scenarios, acceptance criteria, edge conditions, and non-goals.
- Escalate when user intent or success criteria remain unclear.

## Tech Lead / Architect

- Turn approved requirements into `TechPlan`.
- Define architecture, interfaces, migrations, rollout concerns, and test strategy.
- Act as the technical review gate for medium/high-risk work.

## Feature Engineer

- Turn approved plans into `ImplementationPacket`.
- Implement code changes, tests, and delivery notes.
- Escalate when implementation requires a design change.

## QA / Test Engineer

- Turn implementation into `QAVerdict`.
- Validate acceptance criteria, regressions, and residual risk with evidence.
- Escalate when observed behavior conflicts with the approved spec.

## Release / SRE Engineer

- Turn tested changes into `ReleaseChecklist`.
- Review config changes, migrations, rollback, monitoring, and operator notes.
- Stop the release path if QA is not clearly passing or accepted with risk.
