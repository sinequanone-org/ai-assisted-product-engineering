---
name: assurance-design
description: Map threats and invariants to formal proofs, adversarial tests, and explicit limits. Use for security-sensitive behavior or claims that need assurance beyond ordinary functional tests.
license: Apache-2.0
---

# Assurance design

Read the accepted behavior contract and project assurance policy. Identify
assets, actors, attacker control, trust boundaries, entry paths, and residual
risk. Follow data to the final authority check, including imports, replay,
background jobs, and alternate interfaces.

For each material threat, state the attacker goal, preconditions, crossed
boundary, observable harm, required invariant, control, and verification method.
Distinguish a source-grounded concern from a confirmed boundary violation.
Do not infer live exposure from source alone.

For money, authorization, consensus, irreversible actions, and other critical
deterministic controls, complete the required executable formal model and
machine-checked properties before production implementation. Record state,
transitions, quantifiers, environment assumptions, trusted computing base,
toolchain, dependencies, and successful build evidence.

Inspect admitted goals and project axioms. A theorem signature or an assumption
that restates the property cannot close the proof. Explain what the model does
not cover, including runtime adapters and deployment assumptions.

Define how runtime values and transitions correspond to the model. Prefer direct
use of verified transitions when practical. Otherwise require independent
conformance cases and generated or adversarial traces. Finite tests cannot be
reported as a universal refinement proof.

For demand, human judgment, or model quality, record why formal proof does not
apply and choose an empirical study, evaluation, or qualified review. Do not
create a meaningless proof to fill a table. Missing tooling does not make an
applicable proof obligation disappear.

Use existing trusted libraries before adding dependencies. Verify new package
identity, provenance, license, maintenance, install behavior, and pinned version.
Do not replace specialized cryptography with a small custom implementation.

Use bounded, authorized tests with dummy principals and data. Do not probe live
systems as a side effect of a design review. Output the threat-to-invariant-to-
evidence mapping, residual risks, and exact obligations that block delivery.
