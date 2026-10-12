---
name: behavior-specification
description: Define observable behavior, invariants, and acceptance cases before a feature or behavior change. Use for APIs, user flows, state transitions, data formats, or compatibility changes.
license: Apache-2.0
---

# Behavior specification

Read the accepted requirement, current specification, relevant architecture
decisions, and implementation boundary. Identify intended behavior separately
from observed behavior. Record a conflict before choosing which artifact to fix.

Define only the changed contract and its dependencies. Include:

- Actors, roles, and authority to perform each operation.
- Inputs, schema, normalization, limits, and validation order.
- States, transitions, outputs, errors, and recovery.
- Invariants, concurrent operations, retries, replay, and idempotency.
- Privacy, retention, observability, and resource limits.
- Compatibility, migration, and rollback or safe recovery.

Give each requirement and acceptance case a stable ID. Describe externally
observable success, boundary, failure, and recovery cases. For a user flow,
include accessibility and usable error handling. Give performance constraints
units, workloads, and thresholds.

For a parameterized upstream algorithm, bind the exact instance and source
revision. Specify the conformance oracle and old-format behavior. Never accept
new constants or serialized bytes solely because the current code emits them.

For probabilistic or model-dependent behavior, define evaluation data, labels,
error costs, uncertainty, abstention, containment, and version changes. Do not
write a deterministic guarantee for behavior the system cannot guarantee.

Document consequential architecture choices with alternatives and tradeoffs.
Map each acceptance case to a planned proof or test. Identify launch-blocking
decisions and their owners. Reuse an existing contract for a narrow correction.

Ready means the behavior and oracle are clear enough for someone else to reject
a wrong implementation. A list of function names or a prose aspiration is not a
complete specification. Reopen affected assurance when the contract changes.
