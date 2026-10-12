---
name: product-workflow
description: Start or resume a product development work item by selecting its risk class, evidence gates, and relevant workflow skills. Use for scoped delivery work, not unrelated questions or general conversation.
license: Apache-2.0
---

# Product workflow

Read the repository instructions, accepted project policy, current work item,
relevant decisions, and current source state. Treat prior summaries as pointers
to evidence. Do not overwrite unrelated work.

State the audience, problem, expected outcome, scope, non-goals, and success
measure. Reuse existing product records. Distinguish user decisions from agent
proposals and assumptions. Do not change the product to make delivery easier.

Classify the effects as editorial, routine, material, or critical. Money,
authorization, consensus, privacy controls, and irreversible actions require
critical assurance even when the patch is small.

Select only the applicable skills if they are available:

- `product-discovery` for a new problem, audience, or material scope decision.
- `research-evidence` when research or measurements determine a claim or choice.
- `behavior-specification` for observable behavior changes.
- `assurance-design` for threats, invariants, and required formal assurance.
- `test-first-delivery` for production implementation.
- `conformance-review` for checking the contract against the implementation.
- `release-evidence` for readiness or an authorized release.

If a needed skill is unavailable, use the accepted project policy and report the
gap. Do not pretend it was loaded. A docs correction needs source and document
checks; it does not need a new product dossier or application test run.

Track Formalized, Specified, Implemented, Tested, and Released separately. Use
`not_started`, `draft`, `in_progress`, `blocked`, `done`, or `not_applicable`.
Done needs evidence; not-applicable needs a scope-specific reason.

Identify dependencies and required gates before implementation. When a decision
is missing, continue independent authorized work and ask only for the decision
that affects the result. Preserve prior authorization across sessions.

Before handoff, record source identity, dirty changes, decisions, checks, open
gates, and next dependency. Finish or stop task-owned processes. Report actual
results and dependency changes. This skill grants no commit, push, publication,
deployment, spending, or messaging permission.
