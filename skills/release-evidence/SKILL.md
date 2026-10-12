---
name: release-evidence
description: Assess release readiness or carry out an already authorized release using current checks, artifact identity, migration, recovery, and operating evidence. Readiness review alone does not authorize publication or deployment.
license: Apache-2.0
---

# Release evidence

Read the project release policy, work-item state, current candidate, and existing
authorization. Identify the exact action and target. Do not repeat an approval
request already satisfied; do not infer deployment permission from implementation
or readiness work.

Verify required specification, assurance, implementation, test, and review
evidence for this candidate. Check raw outcomes and approved exceptions.
Cancelled runs, stale green runs, build-only checks, and missing logs cannot
establish a required test pass.

Identify the artifact digest, source revision, build configuration, dependency
resolution, target environment, and operator. Check migration, rollback or safe
recovery, health thresholds, and observability. For irreversible state or wire
changes, define when rollback becomes unsafe.

Ensure user-facing docs and claims describe the delivered scope. Keep prototype,
local, merged, and deployed status separate. Do not infer deployment from a PR
merge, or privacy and security from a component benchmark.

If release is authorized and required gates pass, execute within that scope.
Bind the action to the checked artifact and retain actual release, smoke, and
health results. If a required gate fails, stop the dependent action and follow
the authorized recovery procedure. Never self-approve a policy exception.

For readiness-only work, report ready, blocked, or ready with explicitly
authorized exceptions. Do not set Released to done. For a completed release,
link artifact, environment, time, and post-release evidence.

Record user outcomes, support burden, cost, and incidents against the product
success measure. Feed the result into the next product decision. Update the
roadmap and session record without erasing previous evidence.
