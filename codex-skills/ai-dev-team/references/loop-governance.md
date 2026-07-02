# Loop Governance

Use bounded loops, not open-ended loops.

## Required Fields

Every canonical artifact must include:

- `loop_objective`
- `iteration_count`
- `progress_evidence`
- `stop_condition`
- `human_checkpoint`

## Hard Limits

- max same-owner iterations: `3`
- max cross-role rework cycles: `2`
- max failed validation cycles: `2`
- max open questions before pause: `5`

## Mandatory Human Pause Triggers

- same blocker appears twice
- same owner iterates three times without new evidence
- QA and implementation bounce twice without narrowing scope
- architecture or schema changes appear after implementation started
- `session-state.md` cannot name a concrete `next_action`

## Cost Control

- prefer persisted state over replaying long chat history
- avoid parallel specialists unless a second opinion is worth the cost
- stop loops that produce more narration than evidence
- escalate early when uncertainty is not shrinking
