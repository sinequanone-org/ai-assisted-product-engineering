# Evidence based product development

Version: 0.1.0 draft. Date: 2026-10-10.

This method connects product decisions to engineering evidence. It applies to
people and coding agents. It covers discovery, research, specifications,
assurance, implementation, verification, release, and feedback.

Every important claim needs evidence for the exact scope in which it is used.
Every required gate needs a result before work advances past it. The amount of
documentation depends on the change and its risk.

## Package

| File | Purpose |
|---|---|
| [STANDARD.md](STANDARD.md) | Normative method, gates, and evidence rules |
| [HARNESS.md](HARNESS.md) | Bootstrap prompt, skill routing, and enforcement contract |
| [Project policy](templates/project-policy.md) | Local authority, commands, roles, and release rules |
| [Work item](templates/work-item.md) | Requirements, assurance, stage state, and decisions |
| [Evidence record](templates/evidence-record.md) | Reproducible result tied to its source and scope |
| [Evaluation scenarios](evals/scenarios.md) | Behavioral checks for a harness using the method |
| [LICENSE](LICENSE) | Apache License, Version 2.0 |
| [PUBLICATION.md](PUBLICATION.md) | Checks before a public copy |

## Skills

| Skill | Load when |
|---|---|
| [product-workflow](skills/product-workflow/SKILL.md) | Starting or resuming a product work item |
| [product-discovery](skills/product-discovery/SKILL.md) | Choosing a problem, audience, outcome, or product scope |
| [research-evidence](skills/research-evidence/SKILL.md) | Research or measurement informs a decision or public claim |
| [behavior-specification](skills/behavior-specification/SKILL.md) | Defining or changing observable behavior |
| [assurance-design](skills/assurance-design/SKILL.md) | Defining threats, invariants, or formal proof obligations |
| [test-first-delivery](skills/test-first-delivery/SKILL.md) | Implementing a specified behavior change |
| [conformance-review](skills/conformance-review/SKILL.md) | Checking the implementation against its contract |
| [release-evidence](skills/release-evidence/SKILL.md) | Assessing readiness or executing an authorized release |

## Use

1. Keep the package at a stable path in the target repository.
2. Fill in a project policy using the existing project rules and commands.
3. Add the bootstrap prompt from HARNESS.md to the harness instructions.
4. Register the skill directories using the harness's supported skill mechanism.
   If it has none, load the relevant SKILL.md files by path from the prompt.
5. Run the evaluation scenarios in a disposable workspace before adoption.
6. Connect the declared gates to trusted CI and release controls.

Each skill contains its own operational instructions. The standard owns shared
definitions. Load only the skills needed for the current work. A short fix may
need one work record with links to an existing contract and regression test.

## Status and license

Version 0.1.0 is a draft in this tree. There is no release tag.

This package supplies a proposed standard and procedural agent instructions.
It does not install hooks, configure branch protection, or enforce permissions.
A SKILL.md file alone cannot prevent an agent from skipping a gate.

The license is the Apache License, Version 2.0. See [LICENSE](LICENSE) and
[NOTICE](NOTICE). Keep project-specific evidence outside this repository.

Before a public copy, follow [PUBLICATION.md](PUBLICATION.md).
