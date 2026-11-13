# Master roadmap

| Stage | Scope | State |
|---|---|---|
| 1 | Audit GitHub and resume | Complete and verified |
| 2 | Findings and strategy | Complete and verified |
| 3 | Profile README and assets | Complete and verified — merged, rendered, checked |
| 4 | Renames, descriptions, pins, cleanup | Blocked by authentication |
| 5a | Distributed LSM store: engine verification, Raft core, simulation tests | Complete and verified |
| 5b | Distributed LSM store: network transport, server, cluster demo | Pending |
| 5c | ModelOps Hub | Blocked — repository missing |
| 5d | Agent Fault Lab | Blocked — repository missing |
| 6 | Vercel inventory and migration | Blocked by authentication |
| 7 | Portfolio site | Pending |
| 8 | Technical audits and model improvement of ML projects | Pending; training blocked by infrastructure |
| 9 | CI and templates across repositories | Pending (done for lsmkv) |
| 10 | Final audit and consistency check | Pending |

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
