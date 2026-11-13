# Master roadmap

| Stage | Scope | State |
|---|---|---|
| 1 | Audit GitHub and resume | done — `GITHUB_AUDIT.md` |
| 2 | Findings and strategy | done |
| 3 | Profile README and assets | branch `profile-redesign` pushed; awaiting merge |
| 4 | Existing repositories: rename, LICENSE, CI, README gaps | blocked on owner actions (see `PROJECT_STATUS.md`) |
| 5 | Flagship builds | not started |
| 6 | Portfolio site | not started |
| 7 | CI/CD standards across repositories | not started |
| 8 | Final audit | not started |

## Flagship candidates (gap: agents, distributed systems, MLOps, security)

| # | Candidate | Novelty | Usefulness | Difficulty | Research | Deployable | Differentiation | Pick |
|---|---|---|---|---|---|---|---|---|
| A | Agent reliability harness: deterministic replay and fault injection (tool errors, timeouts, corrupted outputs) for tool-using agents, with recovery metrics | high | high | medium | high | yes, runs on local models | high | yes |
| B | Replicated key-value store: Raft consensus on top of the existing LSM-tree engine, with a linearizability checker and partition tests | medium | medium | high | medium | Docker Compose cluster | high | yes |
| C | Model operations layer for the five research services: shared registry, bundle format, canary evaluation, drift alerts, one deployment pipeline | low | high | medium | low | yes | medium; ties the portfolio together | yes |
| D | Intrusion detection under temporal drift on public network-flow data, reusing GraphShield's protocol | medium | high | medium | medium | yes | low; overlaps GraphShield | no |
| E | Multi-agent clinical report analysis with grounded citations | low | medium | medium | medium | needs paid or large models | low; crowded | no |

Order: C first (smallest, makes existing work look connected), then B (extends real code already written), then A.

## Career gaps, by reviewer

- **ML recruiters:** no GPU-scale training evidence, no deployed model with users, no experiment tracking.
- **Software recruiters:** no sustained history on one codebase, no merged open-source pull requests, little Java/C++ despite listing them.
- **Cloud/DevOps recruiters:** Dockerfiles never built, no infrastructure-as-code, no cloud deployment, no certification.
- **Research supervisors:** no accepted paper, no written report or preprint, results are CPU-scale.
- **MS admissions:** needs one finished study with a preprint, a research internship, and letters that can speak to independent work.

Priorities: (1) finish one study properly on a GPU and write it up as a preprint; (2) one merged upstream pull request in a fork already held; (3) one real cloud deployment with a build pipeline; (4) commit little and often.
