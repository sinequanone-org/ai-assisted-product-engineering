---
name: research-evidence
description: Produce reproducible research, comparisons, or benchmarks that support a product decision or technical claim. Use when source quality, configuration, or measurement scope can change the conclusion.
license: Apache-2.0
---

# Research evidence

Start with the decision, question, scope, alternatives, and rejection criteria.
Separate a literature claim, implementation fact, measured result, and prediction.
Read primary evidence before treating a summary or prior agent answer as fact.

Record the source version, date, relevant passage or code, and limitations. Search
for contrary evidence. A reputable source can still describe a different release,
parameter set, or execution path. Verify those identities before transferring a
claim to the current product.

For implementation-dependent claims, identify the exact revision, parameters,
feature flags, dependency locks, caller, and deployed path if known. A function
existing in a library does not establish that the product invokes it.

Before measuring, fix the workload, semantics, security settings, commands,
build profile, hardware, seeds, repetitions, warmup, cache policy, and accounting
boundary. Explain unequal conditions. Keep setup, steady-state work, and complete
artifact costs distinct.

Retain raw outputs, failures, source snapshots, and hashes in a new run directory.
Include relevant dirty changes; a commit ID alone cannot identify them. Do not
overwrite prior evidence or change measured source before its identity is saved.
Use synthetic or permitted data and bound local runs.

Report sample size, units, spread when supported, and uncertainty. Do not infer
production throughput from unrelated component timings or universal behavior
from one run. Verify benchmark input extraction and the measurement boundary
before a long run when either is new or changed.

Write conclusions as observed facts, derived results, hypotheses, targets, or
projections. State what each result permits the decision-maker to conclude.
List unresolved obligations beside the recommendation.

An experiment is complete when its question is answered within scope or the
remaining uncertainty is stated with a concrete next test. A benchmark result
does not close a security proof or product-release gate.
