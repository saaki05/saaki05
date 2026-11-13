# Research contributions

Only what is backed by code and results in a repository is listed. "Claimed novelty" is deliberately conservative.

## lsmkv (grandmaster) — replication tested by deterministic simulation

- **Question.** Can a from-scratch Raft implementation be shown safe by evidence that would fail if it were wrong?
- **Method.** Seeded whole-cluster simulation with partitions, crashes, loss and duplication; online checks for election safety and state machine safety; offline log matching, convergence and a linearizability checker; mutation testing of the harness with three injected bugs.
- **Result.** 150 fault schedules pass. Injected bugs are caught in 40, 59 and 7 of 60 schedules; the stale-read bug is caught only by the linearizability checker.
- **Related work.** Deterministic simulation testing is established practice (FoundationDB; TigerBeetle's simulator); Jepsen and Knossos/Porcupine check linearizability of real systems. Wing and Gong (1993) and Lowe (2017) give the search used here.
- **What is new.** Nothing methodologically. It is a correct, small reproduction of known techniques.
- **Limitations.** No real network, no snapshots, crash model keeps all written state, histories are short.
- **A possible research direction.** Measure detection rate of a catalogue of known Raft bugs as a function of fault-schedule parameters, to say which fault mix finds which bug class cheapest.

## GraphShield, PredictIQ, PaperMind, TerraVision, VisionForge

Each README states its own question, protocol and limits, and none claims a new method. They were not re-audited or re-run in this session; the 18-point technical audit and baseline reports are pending. Known gaps from their status tables: CPU-only training, few seeds, and missing standard benchmarks (Elliptic; OSCD or LEVIR-CD; DIV2K).

Most promising for a workshop paper, in order: PredictIQ (conformal interval validity under operating-condition shift), TerraVision (how much random tile splits inflate change-detection scores), GraphShield once Elliptic is run.

## OncoScan-AI

No contribution can be stated yet: the repository holds one commit and no evaluation artefacts, datasets were not reachable from the build environment, and the figures quoted elsewhere have not been reproduced. Patient-level leakage in the leukemia and histopathology splits must be checked before any number is used.

## Resume projects with no repository

Diabetic Retinopathy, Disease Prediction, Medical Report Analysis and SmartReview have no public code, so they cannot be audited or improved until the code is pushed.
