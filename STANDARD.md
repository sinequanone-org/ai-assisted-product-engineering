# Evidence based product development standard

Version: 0.1.0 draft. Date: 2026-10-10.

## 1. Purpose and terms

The method makes product decisions and delivery claims reviewable. It combines
discovery with specification, assurance, and measured delivery. It does not
promise correct output from a prompt alone.

MUST marks a requirement for conformance with this standard. SHOULD marks a
default that can change with a recorded reason. MAY marks an option.

A work item is one reviewable outcome. Evidence is a retained source or result
that supports a stated claim under stated conditions. An owner is the person or
role accountable for a decision. An agent can prepare a decision without owning
the authority to release, accept risk, or change product scope.

## 2. Start from the user outcome

Before selecting a solution, a work item MUST identify its audience, problem,
expected outcome, constraints, non-goals, and success measure. Existing product
records MAY supply these facts by reference.

For a new product or a material expansion, record the market hypothesis,
alternatives, evidence quality, distribution and cost assumptions, and a study
that can reject the hypothesis. State the decision threshold before collecting
results. A prototype shows feasibility; it does not establish customer demand.

Discovery and delivery can proceed in parallel where their dependencies permit.
Exploratory code MUST be marked as a prototype with a bounded question. It MUST
NOT enter a production path until the applicable delivery gates pass.

## 3. Scale the work to risk

| Class | Examples | Minimum work |
|---|---|---|
| Editorial | Wording, links, non-executable documentation | Verify sources, meaning, links, and affected claims |
| Routine | Local bug fix or behavior-preserving refactor | Existing contract, regression evidence, affected static and integration checks |
| Material | New user flow, interface, storage schema, or dependency | Outcome, behavior contract, threat assessment, traceability, integration and release plan |
| Critical | Money, authorization, consensus, privacy controls, irreversible actions | Material requirements plus explicit invariants, formal assurance for critical deterministic controls, adversarial conformance, migration and recovery evidence |

Select the highest applicable class from the actual effects. A one-line
authorization change can be critical. A documentation change to a security claim
still needs evidence for that claim. File extension and patch size alone MUST
NOT decide the class.

For properties outside a formal model, such as demand or model judgment, record
why formal proof is not applicable and use a study, evaluation, or qualified
review. Lack of proof tooling is not a reason to mark a required proof as done.

## 4. Maintain one authority for each decision

The project policy MUST name the authorities for product scope, runtime
behavior, formal claims, release policy, and measured evidence. Use links to
these records instead of copying mutable rules and numbers.

An accepted specification defines intended behavior. Source inspection and
execution establish observed behavior. A proof establishes its theorem under
its assumptions. None of these automatically establishes the other two.

When records disagree, record the conflict and its effect. Obtain the required
decision or correct the defective artifact before dependent work advances.
Do not weaken a requirement or rewrite a test solely to fit the implementation.
An approved behavior change can revise the contract with a recorded rationale.

An upstream implementation MUST be identified by revision, configuration,
parameters, and relevant source or artifact digest. A library name or algorithm
name does not identify an instance. A newer upstream revision triggers review;
it does not silently replace the project's accepted dependency or wire format.

## 5. Specify observable behavior

Before production implementation, the contract MUST state the relevant actors,
authority, inputs, outputs, errors, limits, state transitions, and invariants.
Include concurrency, retries, replay, idempotency, data retention, and migration
where they affect the behavior.

Assign stable requirement and acceptance IDs. Each acceptance criterion MUST
describe an observable result. Cover success, boundaries, failure, and recovery.
Quality requirements need units and conditions, such as latency at a stated
workload and percentile. Accessibility and usability belong in user-flow criteria.

Record architecture decisions when alternatives have material consequences.
Include the options rejected, evidence, tradeoffs, and a condition for revisiting
the choice. Do not create a new architecture record for every local edit.

For model-dependent behavior, specify uncertainty, abstention, containment,
evaluation data, labels, error costs, and model/version changes. A citation
checker can establish citation validity without establishing semantic truth.

## 6. Design assurance before implementation

Map assets, adversaries, trust boundaries, abuse cases, controls, and residual
risk. Trace each material threat to an invariant and a check. Include routes that
can bypass the normal user path, such as replay, imports, background jobs, and
direct API access.

For critical deterministic controls, write an executable formal model and
machine-check the required properties before production implementation. Record
the model, quantifiers, assumptions, trusted computing base, proof dependencies,
toolchain, and build result. A theorem declaration, admitted goal, or axiom that
restates the desired property MUST NOT count as a completed proof.

State what the model excludes. Prefer executing verified transitions directly
where practical. Otherwise identify the mapping from runtime states and inputs
to the model and test that mapping. Finite trace comparisons MUST NOT be called
a universal refinement proof.

Security-critical dependencies need verified identity, provenance, maintenance,
license, install behavior, and pinned resolution. Prefer established libraries
for cryptography and other specialized controls; a small line count is not a
reason to write a replacement.

## 7. Implement through failing behavior tests

For new or changed behavior, write and run a test before production code. Confirm
that it fails for the intended missing or incorrect behavior. An unrelated build
failure is not useful red evidence. Implement the smallest coherent change, run
the test to green, then refactor while preserving the result.

Tests SHOULD derive expectations from the contract or an independent oracle.
Copying the implementation into a test does not provide independent evidence.
Preserve useful regressions. Change expected values only with a contract change
or independently supported correction to the oracle.

For a refactor, run existing behavior tests before and after. For editorial work,
use document checks. Do not invent a failing application test for a text change.
Do not claim TDD if the test was first run after the implementation existed.

## 8. Verify at distinct boundaries

| Check | Supports | Does not establish by itself |
|---|---|---|
| Unit and property tests | Cases and sampled properties of a component | All inputs or complete product behavior |
| Formal proof | A theorem about a model under assumptions | Runtime conformance or deployment correctness |
| Conformance tests | Agreement with a specification or independent vectors | Universal equivalence unless separately proved |
| Black-box tests | Observable behavior through a public boundary | Coverage of hidden or unreachable paths |
| Integration and end-to-end tests | Composition of identified components and routes | Correct deployment in an untested environment |
| Adversarial tests | Rejection or containment of specified abuse cases | Absence of every vulnerability |
| Benchmarks | Cost for the measured workload and configuration | Security or performance outside that scope |
| Product evaluation | Observed user outcomes in the studied population | Market-wide demand or causation without study support |

Run the project policy's applicable format, lint, type, proof, test, and document
checks. Test supported feature combinations and production paths. A mock or
demo path MUST NOT support a claim about the production path.

For high-risk changes, require review by someone other than the author, with
access to raw evidence. Record reviewer identity and scope. Another role in the
same agent conversation is self-review. Multiple model opinions do not replace
an independent oracle or establish scientific peer review.

## 9. Bind evidence to the claim

Every required result MUST identify its claim, source revision, relevant dirty
changes, configuration, method or command, environment, outcome, and artifact
location. Use content hashes when the source or artifact can otherwise change.
Record failures and exclusions beside the result.

Use `pass`, `fail`, `blocked`, `not_run`, and `not_applicable` for check results.
An applicable timeout, cancellation, missing log, or skipped check is not a pass.
A not-applicable result needs a reason tied to the scope and project policy.

Research claims MUST distinguish observed facts, derived results, hypotheses,
targets, and projections. Preserve primary sources, dates, contradictory
evidence, uncertainty, and the limits of each source. A model-generated summary
is a lead to verify, not a primary source.

Benchmarks MUST preserve raw results and state the workload, source, parameters,
build, hardware, repetitions, warmup, cache policy, and accounting boundary.
Compare equivalent semantics and security settings. State uncertainty; one
sample does not establish a distribution. Do not overwrite a retained run.

Relevant source, requirement, parameter, toolchain, or configuration changes MUST
invalidate dependent evidence until impact is assessed. Carry evidence forward
only with a recorded reason that its premises remain unchanged.

## 10. Track stage state separately

Track `Formalized`, `Specified`, `Implemented`, `Tested`, and `Released` for each
work item. These are separate evidence dimensions, not percentages of one task.
Discovery, specification, and model work may iterate before delivery gates pass.

Use `not_started`, `draft`, `in_progress`, `blocked`, `done`, or `not_applicable`.
Every done stage needs evidence. Every not-applicable stage needs a reason.

| Gate | Conditions to advance |
|---|---|
| Ready for implementation | Outcome and contract are defined; material threats and acceptance cases are mapped; required formal assurance passes; blocking choices are resolved |
| Ready for review | Source is identified; applicable checks pass; requirement, proof, test, and implementation links agree |
| Ready for release | Required review and checks pass for the release candidate; migration, recovery, observability, and authorization are established |
| Released | Artifact and environment are identified; authorized release occurred; smoke and health results are retained |

Missing required evidence blocks the dependent gate. Work on independent tasks
may continue. A known baseline failure remains a failure; the project owner can
record an exception with scope, reason, compensating control, owner, expiry, and
follow-up. Report the exception beside readiness. Never rename it a green check.

Do not grant an exception to fabricated evidence, missing action authorization,
or a claim stronger than its evidence. A required critical proof remains required
unless the accepted product scope or assurance policy changes explicitly.

## 11. Release and learn

A merge is not a deployment. A local build is not a release. For a release,
record artifact identity, target environment, dependencies, migration, rollback
or safe recovery, monitoring thresholds, and the accountable operator.

For an irreversible format change, explain when rollback becomes unsafe and how
to recover. Do not deploy incompatible participants together without an approved
compatibility procedure.

Compare post-release behavior and user outcomes with the stated success measure.
Record incidents, support burden, cost, and negative feedback. Use this evidence
to continue, revise, or stop the product hypothesis.

Update the affected docs, roadmap, and session record. Keep proposed, local,
merged, released, and observed states distinct. Commit, push, publish, and deploy
only within the user's actual authorization and the project policy.

## 12. Enforce and improve the method

The harness MUST route applicable work to the right instructions and preserve
work state across sessions. Trusted checks MUST evaluate declared evidence and
current source. Permissions and protected release controls MUST prevent the
working agent from self-authorizing restricted actions.

An agent-authored checklist is a report. It is not an independent enforcement
boundary. Keep governance for gate definitions separate from an agent's ability
to edit implementation files.

Measure escaped defects, reopened requirements, stale evidence, failed releases,
user outcomes, and time spent on checks. Do not optimize for document volume,
test count, or reviewer scores alone. Version the method and evaluate changes
against realistic tasks, including cases where the right action is to stop.
