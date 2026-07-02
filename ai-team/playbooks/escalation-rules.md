# Escalation Rules

Escalation exists to protect flow, not to hide uncertainty.

## Escalate To The Human Immediately

- the task changes roadmap priority or business commitment
- requirement ambiguity would alter implementation scope materially
- a medium/high-risk technical plan is ready for approval
- merge or release is being requested

## Escalate Across Agents

- `Orchestrator -> Product Analyst`: user intent or acceptance criteria are unclear
- `Orchestrator -> Tech Lead`: scope is clear enough to skip product analysis
- `Product Analyst -> Human`: requirement tradeoff changes user value or timeline
- `Tech Lead -> Human`: architecture, compatibility, migration, or reliability risk needs approval
- `Feature Engineer -> Tech Lead`: implementation reveals design gaps or unsafe deviations
- `QA -> Tech Lead`: behavior conflicts with the approved spec or regression risk is significant
- `Release / SRE -> Human`: operational risk is not acceptable without an explicit decision

## Escalation Triggers That Must Be Recorded

- blocked by external dependency
- missing required artifact field
- hidden schema or API compatibility risk
- test evidence is incomplete or contradictory
- rollback path is missing or unproven

## Escalation Message Format

When escalating, always include:

- what is blocked
- why the current owner cannot safely proceed
- which decision is needed
- what options exist
- what happens if no decision is made now
