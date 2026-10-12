---
name: conformance-review
description: Check an implementation against its accepted requirements, formal model, independent vectors, and public behavior. Use for verification and readiness review, especially when component success may hide integration gaps.
license: Apache-2.0
---

# Conformance review

Start from the accepted contract and source identity. Build or update the map
from requirement to acceptance case, invariant, proof, test, implementation, and
result. Empty required links are gaps, not completed checklist rows.

Check that oracles are independent of the implementation under test. Pin the
upstream revision, parameters, generator, and vectors when comparing an external
standard. Check error behavior, field and size boundaries, and obsolete-format
rejection where the contract requires it.

Trace the real call path from the public interface through validation, storage,
replay, and consumption. A library test does not establish that callers use the
library. A build with mocks cannot alone establish production behavior.

Run black-box cases through the supported public boundary. Include invalid,
unauthorized, duplicate, stale, and partially failed operations as applicable.
Run integration checks for actual composition and supported feature combinations.
State the environment and any dependency replaced by a stand-in.

Review formal assumptions and the mapping to runtime behavior. Identify what
the proof excludes. Never convert a model theorem or finite trace comparison
into a claim of complete implementation correctness.

Verify raw logs, exit status, exclusions, and candidate identity. Missing,
cancelled, timed-out, or required skipped checks cannot count as passes. A known
baseline failure needs a visible exception if policy permits one.

Record reviewer identity and scope. A second role played by the author is
self-review. Do not invent independent review or use model scores as proof.
When required review is unavailable, report that gate as blocked.

Return a readiness verdict with supported claims, concrete mismatches, open
obligations, and evidence references. Reopen affected gates when the contract,
implementation, parameters, or test oracle changes.
