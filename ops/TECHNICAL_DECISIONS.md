# Technical decisions

| # | Decision | Reason |
|---|---|---|
| 1 | Profile changes go to a branch, not straight to `main` | The README depends on external image services that could not be previewed; the owner should see it rendered first |
| 2 | Operations documents live on `portfolio-ops`, not on the profile's `main` | They include candid assessments that should not render on the public profile |
| 3 | The five existing research repositories are the featured work; no new projects in those areas | They already have tests, CI and honest status tables; their weakness is naming, compute scale and history |
| 4 | No result figures on the profile README | Numbers stay in each repository's generated report, next to the protocol that produced them |
| 5 | OncoScan-AI figures and the unpublished paper are not mentioned | Not yet backed by artefacts in the repository |
| 6 | Email omitted from the profile | Two different addresses exist in current materials; LinkedIn is used until confirmed |
| 7 | Facebook, Instagram and X links removed | Personal accounts, outside a professional profile |
| 8 | New flagships build on existing code (LSM store, the five services) | Shows continuity instead of more one-day repositories |
| 9 | Profile branch merged to `main` by push after the render check | Owner instructed the merge; no private data, no accuracy figures, no paused links in the file |
| 10 | GitHub stats cards removed | The public stats service returned no image when rendered on GitHub; GitHub's own contribution graph sits directly below the README |
| 11 | Raft written as an I/O-free state machine and tested in a seeded simulator before any networking | Makes every failure reproducible from a seed; the transport is added afterwards around unchanged logic |
| 12 | Reads go through the Raft log | Linearizable without leases or clock assumptions; costs one log write per read |
| 13 | A MANIFEST file, not a directory scan, defines live SSTables | Lets flush and compaction be installed atomically |
| 14 | The harness is tested against injected bugs | A safety test that has never failed is not evidence |
| 15 | SQLite with synchronous=FULL as benchmark baseline | Same durability contract, standard library, a store people know |
