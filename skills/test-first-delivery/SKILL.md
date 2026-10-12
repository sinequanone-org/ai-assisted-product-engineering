---
name: test-first-delivery
description: Implement a specified behavior change through failing tests, minimal code, and relevant regression checks. Use for features and defect fixes; use existing behavior checks for refactors and document checks for editorial work.
license: Apache-2.0
---

# Test first delivery

Read the contract, acceptance cases, relevant source, and project check commands.
Confirm that required specification and formal assurance gates have passed.
Keep exploratory prototypes outside production paths until those gates pass.

Write a behavior test using the contract or an independent oracle. Run it before
production edits and record why it fails. An unrelated toolchain or build failure
does not establish the intended regression. A test that already passes does not
justify a claimed fix; investigate the reproduction.

Implement the smallest coherent change. Run the focused test to green, refactor,
then run the relevant regression, lint, type, proof, and integration checks from
project policy. Test negative and boundary cases. Include replay and concurrency
when the state model permits them.

For a refactor, use passing baseline behavior tests before and after. For a text
edit, verify meaning, sources, links, and applicable document checks. Do not run
unrelated application suites merely to make the work look tested.

Do not weaken a norm, invariant, limit, test, or gate to obtain green output.
Change expected values only after an independently supported oracle correction
or accepted contract change. State that reason with the updated evidence.

Preserve user changes and existing conventions. Prefer existing dependencies.
If a new dependency is needed, follow project provenance and approval rules.
Keep secrets and private names out of code, fixtures, and logs.

Record exact source and configuration for the results. Changes after a run need
an impact assessment and affected reruns. Do not report cancelled or timed-out
checks as passing. Report pre-existing failures with baseline evidence.

Output the patch, contract references, red and green results, broader checks,
and remaining limits. Update affected docs and work state. Commit and push only
within actual user authorization and project policy.
