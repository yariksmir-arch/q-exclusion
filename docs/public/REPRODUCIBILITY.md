# Reproducibility

## Supported local environment

The complete route is verified on Windows 11 with Python 3.12.10 and Windows PowerShell 5.1. Python uses only its standard library; PowerShell is needed for the preserved 178-check suite. No external data, account, package installation or service is required.

From the public repository root:

~~~powershell
python -B research/verification/verify_public.py
python -B research/regression/canonical_regression.py
python -B research/regression/portable_regression.py
python -B research/verification/verify_public.py
~~~

The canonical runner preserves the original PowerShell suite and its separate Python suites. The portable runner adds the construction, interface, coordination, compression and negative semantic controls. Some Python suites consequently run twice; their counts must not be added as independent evidence.

## Suite commands

| Suite | Command after python -B | Evidence |
|---|---|---|
| Canonical Windows replay | research/regression/canonical_regression.py | 178 PowerShell witnesses plus separately counted control, semantic, articulation, question and incidence suites |
| All Python suites | research/regression/portable_regression.py | Same Python suites plus the four model suites below and semantic-transition controls |
| Construction/maintenance | research/verification/endogenous_check.py | 116 finite assertions; model tables and ablations |
| Operational interfaces | research/verification/interface_check.py | Exact finite quotient/kernel/clamp controls |
| Coordination | research/verification/coordination_check.py | Finite relation joins, deletion and relabelling controls |
| Interface questions | research/verification/interface_question_check.py | Residuals, compression and explicit representation premises |
| Transport scope | research/regression/transport_scope_check.py | Exhaustive small refinement/relabelling diagrams and removal controls for PI6, PI7, noncanonical sections and partial-operation domains |
| Semantic transition controls | research/regression/semantic_transition_check.py | Counterexamples to illegitimate inference steps, including the missing fixed-profile hypothesis |

These commands are read-only. Optional explicit output flags in a model script are unnecessary. Checks validate named witnesses and bounded enumerations; general claims require the written proofs in the formal guide. No experiment tests or confirms SS.

## Linux, macOS and CI

The Python route uses platform-neutral standard-library APIs and is prepared for Linux/macOS. Those operating systems have not been executed locally in this release pass. The full canonical runner still invokes Windows PowerShell; the Python-only route does not replace its 178 checks. No unverified PowerShell port is advertised.

The [CI workflow](../../.github/workflows/verify.yml) runs the full route on Windows and the Python route on Ubuntu/macOS, using pinned action commits and a read-only token. Hosted CI has not yet run; it could also run in a private repository after an explicitly authorized upload. Local verification remains independent of it.

## Snapshot and archive integrity

MANIFEST.json lists every payload path, byte count, SHA-256 and effective license, plus the fixed source commit and frozen-file hashes. It excludes itself from its per-file hash list to avoid self-reference. The archive's external SHA-256 covers the manifest too. The verifier rejects extra files, missing files, hash changes, symlinks, broken local Markdown links and non-stdlib Python imports. It needs no internal history.

To reproduce the content ZIP, choose a new path outside the repository:

~~~powershell
python -B research/verification/reproduce_archive.py ../q-exclusion-reproduced.zip
~~~

The ZIP has sorted paths, fixed timestamps/modes and stored bytes without compression, so it does not depend on a compression-library version. It excludes .git. An extracted ZIP is a complete verification environment and can be initialized as a new independent Git repository.

To reconstruct from public Git instead, use git clone --no-local with an empty remote or the reviewed public repository location. This candidate has a single new initial commit and no remote, submodule, alternates or shared object store. A clean clone and an extracted archive were verified separately during preparation. They require no file from the research source checkout.

For an effective-license check, run:

~~~powershell
python -B research/verification/verify_public.py --require-licensed
~~~

MIT and CC BY 4.0 are active under the owner’s approval recorded in LICENSE-STATUS.json, with scope and attribution in [LICENSE-CONTENT.md](../../LICENSE-CONTENT.md) and [NOTICE.md](../../NOTICE.md). The --require-approved flag additionally checks authorization for Codex to upload, publish or push. It currently fails with PUBLICATION_NOT_AUTHORIZED because those actions remain prohibited. This agent-action restriction does not limit recipients’ rights under the effective licenses.
