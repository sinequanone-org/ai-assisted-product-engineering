# Evidence record template

This record links a result to a claim. Unfilled fields do not count as evidence.
Use explicit not-applicable reasons for fields outside the result's scope.

## Identity

- Evidence ID and date:
- Claim and linked requirement or gate:
- Claim type: observed, derived, hypothesis, target, or projection:
- Work-item ID and source revision:
- Relevant dirty-source snapshot and content hashes:
- Dependency locks, submodule revisions, and generated inputs:
- Parameters, feature flags, and artifact identity:
- Toolchain and non-secret environment details:

## Method and result

- Primary source with version, date, and relevant passage:
- Exact command or review procedure and working directory:
- Expected result and oracle provenance:
- Actual result, exit status, start, end, and timeout status:
- Result state: pass, fail, blocked, not_run, or not_applicable:
- Raw logs or artifacts and their digests:
- Author, reviewer, and review scope:
- Exclusions, assumptions, contradictory evidence, and limitations:

For a benchmark, add workload, hardware, build profile, repeats, seeds, warmup,
cache policy, measurement units, accounting boundary, and uncertainty. For a
proof, add theorem, assumptions, trusted computing base, and successful build.

## Validity

- What this evidence establishes:
- What remains untested or unproved:
- Changes that invalidate the result:
- Carry-forward decision and rationale, if used for a later candidate:

Store only the environment details needed to reproduce the result. Do not store
credentials, private user paths, unrelated customer data, or a full environment
dump. Sanitize publication copies without changing the result's meaning.
