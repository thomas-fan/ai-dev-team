# ReleaseChecklist

Use this to determine whether a change is operationally safe to merge and ship.

## Required Fields

- `objective`:
- `inputs`:
- `constraints`:
- `artifacts_out`:
- `done_criteria`:
- `open_questions`:
- `escalation_trigger`:

## Task-Specific Fields

- `qa_status`:
- `config_changes`:
- `migration_plan`:
- `rollback_plan`:
- `monitoring_watch_items`:
- `release_notes`:
- `release_recommendation`:
- `loop_objective`:
- `iteration_count`:
- `progress_evidence`:
- `stop_condition`:
- `human_checkpoint`:

## Template

```md
# ReleaseChecklist

- objective:
- inputs:
- constraints:
- artifacts_out:
- done_criteria:
- open_questions:
- escalation_trigger:
- qa_status:
- config_changes:
- migration_plan:
- rollback_plan:
- monitoring_watch_items:
- release_notes:
- release_recommendation:
- loop_objective:
- iteration_count:
- progress_evidence:
- stop_condition:
- human_checkpoint:
```
