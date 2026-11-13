# Portfolio architecture

```mermaid
flowchart TB
  subgraph Research[Research engineering — data → models → service]
    GS[graphshield] ; PQ[predictiq] ; PM[papermind] ; TV[terravision] ; VF[visionforge]
  end
  subgraph Health[Healthcare AI]
    ON[oncoscan-ai]
  end
  subgraph Systems[Systems]
    LSM[lsm-kv-store] --> RAFT[raft-kv — planned]
    CH[chennai-insights-dashboard]
  end
  subgraph Ops[Production ML — planned]
    HUB[modelops-hub]
  end
  subgraph Agents[Agents — planned]
    AFL[agent-fault-lab]
    AEG[aegis-support-agents — hackathon]
  end
  subgraph Products[Products]
    BS[bhoomisetu] ; SS[SilentSync]
  end
  Research -- model bundles --> HUB
  ON -- model bundles --> HUB
  HUB -- metadata store --> RAFT
  AEG -. test subject .-> AFL
```

Shared conventions already present in the research repositories, to be carried to the rest: three packages with one-way dependencies, `pyproject.toml` per package, `ruff`, `pytest`, a `ci.yml` workflow, a status table in the README, results generated from JSON into `REPORT.md`.

Products and the dashboard stay separate; they are not forced into the model pipeline.
