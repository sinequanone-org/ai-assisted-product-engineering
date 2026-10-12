# Work item template

Use the relevant sections. For a small fix, link the existing requirement and
contract. Do not copy an entire product dossier into this record.

## Outcome

- ID, title, owner role, priority:
- User request and authorized scope:
- Audience, problem, outcome, and success measure:
- Evidence for the need, or explicit hypothesis:
- Constraints and non-goals:
- Risk class and reason:
- Dependencies and current source identity:
- Applicable project policy and method version:

## Contract and traceability

| Need | Requirement | Acceptance case | Specification | Threat or invariant | Proof or not-applicable reason | Independent test or oracle | Implementation | Evidence |
|---|---|---|---|---|---|---|---|---|
| Fill | Fill | Fill | Fill | Fill | Fill | Fill | Fill | Fill |

Record actors, authority, states, inputs, outputs, errors, limits, and recovery
where they affect the change. Link design choices and compatibility decisions.

## Stage state

Use `not_started`, `draft`, `in_progress`, `blocked`, `done`, or `not_applicable`.
These columns are separate. They do not imply a fixed document-writing order.

| Stage | State | Evidence or reason | Open obligation |
|---|---|---|---|
| Formalized | not_started | Fill | Fill |
| Specified | not_started | Fill | Fill |
| Implemented | not_started | Fill | Fill |
| Tested | not_started | Fill | Fill |
| Released | not_started | Fill | Fill |

## Check plan and results

| Gate ID | Required for this change | Command or review method | Result | Evidence record | Candidate identity |
|---|---|---|---|---|---|
| Fill | Fill | Fill | not_run | Fill | Fill |

Check results: `pass`, `fail`, `blocked`, `not_run`, or `not_applicable`.
Record red and green behavior runs separately. Explain the expected red failure.

## Decisions, exceptions, and invalidation

| Decision or conflict | Status | Authority | Rationale and evidence | Blocks which work |
|---|---|---|---|---|
| Fill | proposed | Fill | Fill | Fill |

For an exception, record its scope, compensating control, expiry, and follow-up.
Record which evidence becomes stale when its premises change.

## Release and feedback

- Readiness verdict and remaining blockers:
- Authorized action, artifact identity, and target environment:
- Migration and rollback or safe recovery:
- Smoke and health results:
- Measured user outcome and next decision:
- Documentation, roadmap, and session record links:
