# Project policy template

Copy this file into the target project's documentation. Fill each field before
using it as policy. Preserve stricter existing rules. Do not invent commands or
approval roles. This template grants no authorization.

## Identity and authority

- Policy version, status, and acceptance record:
- Repository and allowed working scope:
- Method version and local path:
- Product outcome and scope authority:
- Behavior specification and decision authority:
- Formal claim authority:
- Evidence storage and retention:
- Check-definition authority:
- Risk acceptance and release authority:
- Existing user authorization for this work:
- Commit, push, publication, and deployment rules:

## Classification and checks

Choose checks from existing build and CI configuration. Use separate rows for
incompatible feature combinations. For each row, define when it is required.

| Gate ID | Applicable scope | Exact command and working directory | Toolchain and configuration | Required result | Trusted runner or owner |
|---|---|---|---|---|---|
| Fill | Fill | Fill | Fill | Fill | Fill |

Include document checks, format, lint, typecheck, behavioral tests, conformance,
integration, production build, formal proof, and security checks as applicable.
State test timeout and resource budgets. Do not infer test coverage from a build.

## Assurance and review

- Critical deterministic controls requiring formal assurance:
- Formal tools, model scope, assumptions, and trusted computing base:
- Independent oracles and test-vector provenance:
- Review requirements and reviewer independence:
- Exception authority, scope, expiry, and follow-up process:
- Treatment of unavailable checks and known baseline failures:

## Delivery and operations

- Supported build, feature, platform, and dependency matrix:
- Release candidate identity and artifact digest method:
- Migration, rollback, irreversible steps, and safe recovery:
- Smoke checks, health thresholds, and operator:
- Outcome metric, feedback source, and review cadence:
- Required documentation, roadmap, and session records:

## Enforcement status

| Control | Location | Active or proposed | Last rejection-path test and evidence |
|---|---|---|---|
| Skill routing | Fill | Fill | Fill |
| Trusted CI gates | Fill | Fill | Fill |
| Protected merge | Fill | Fill | Fill |
| Release permissions | Fill | Fill | Fill |

Unfilled fields are unresolved configuration. They cannot establish a passed
gate or a mechanically enforced policy.
