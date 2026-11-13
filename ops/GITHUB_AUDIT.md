# GitHub audit — saaki05 (13 November 2026)

40 public repositories: 28 own, 12 forks. All 28 own repositories were cloned and inspected (tree, README, history, CI, tests). No committed secrets or `.env` files found by pattern scan.

## Inventory

| Repository | What it is | Commits | Tests | CI | Class |
|---|---|---|---|---|---|
| project-1- (GraphShield) | GNN fraud detection, leak-audited protocol | 6 | yes | passing | 2 — feature; rename |
| project-2 (PredictIQ) | RUL prediction with conformal intervals under shift | 4 | yes | yes | 2 — feature; rename |
| project-3 (PaperMind) | SciFact evidence retrieval ablation | 6 | yes | yes | 2 — feature; rename |
| project-4 (TerraVision) | Satellite change detection, split leakage | 7 | yes | yes | 2 — feature; rename |
| project-5 (VisionForge) | Budgeted super-resolution comparison | 6 | yes | yes | 2 — feature; rename |
| oncoscan-ai | Multi-modality cancer screening suite | 1 | 3 files | no | 3 — feature; needs CI, metrics evidence, history |
| grandmaster | LSM-tree key-value store | 2 | 6 files | no | 2 — feature; rename, add CI |
| chennai-insights-dashboard | Traffic dashboard, simulated feed, Pages deploy | 1334 (1328 bot) | no | cron | 3 — feature; tests, stop bot commits on main |
| bhoomisetu-app- | Flutter + Node marketplace | 32 | 18 files | no | 3 — feature; CI, README depth |
| bhoomisetu | Earlier copy of the same app (same root commit) | 7 | 13 files | no | 5 — duplicate, archive |
| SilentSync | Flutter accessibility app | 4 | 5 files | no | 4 — keep; sign model absent |
| Great-Agent-hackathon- (Aegis) | Multi-agent support triage | 1 | no | no | 4 — keep as hackathon record |
| hacka (FusionGuard AI) | Cyber + transaction anomaly prototype | 1 | no | no | 4 — keep; rename |
| adhikar-ai | Legal-rights assistant, hackathon | 2 | no | no | 4 — keep |
| IDBI-innovate | Banking simulation; 24 commits by a teammate, none by saaki05 | 24 | 3 files | no | unpin; state team role or archive |
| GEN-AI-LLM-tricks- | Course lab record (12 experiments) | 6 | no | no | 6 — coursework, archive or leave unpinned |
| dav-record-work- | Course lab record | 1 | no | no | 6 |
| tunix | Gemma fine-tuning data prep | 2 | no | no | 6 — merge with the empty tunix-hack repo |
| flowforge-chat-proxy | 40-line API proxy | 1 | no | no | 6 |
| Saaketh-Portfolio / saaki-resume-portfolio | Identical portfolio sites | 1 each | — | no | 5 — keep one, replace in Stage 6 |
| saaketh05 | Copy of the profile README | 2 | — | — | 5 — archive |
| Prashant, hackathon-work-, Real-Time-Chennai-Insights-Dashboard- | Empty | 0 | — | — | 6 — delete |
| Googletunixhack-summrization-, Week-1-cs50 | README only | 1 | — | — | 6 — archive |
| 12 forks (datafusion, jax, PictoPy, …) | No evidence of merged upstream contributions checked yet | — | — | — | unpin; keep only forks with merged pull requests |

## Findings that matter most

1. The five strongest repositories are named `project-1-` to `project-5`.
2. Pinned set is weak: a bare fork (datafusion), a teammate-authored repo (IDBI-innovate), and the older duplicate of BhoomiSetu.
3. History is thin: most projects are 1–7 commits made in one or two days. Reviewers read that as bulk upload. Fix going forward with incremental work, not by rewriting history.
4. `saakimainresume.pdf` in both portfolio repositories publishes a phone number.
5. Resume says "Bachelor of Science"; the degree is B.E. Email differs between resume (`saakethcse05`) and old profile README (`saakethcsse05`).
6. Resume lists Diabetic Retinopathy, Disease Prediction, Medical Report Analysis, SmartReview, E-Commerce and Student Utility projects with no public repository. The resume dashboard is "Bengaluru"; the repository is Chennai.
7. Both Vercel portfolio links could not be reached from the audit environment — verify.
8. No project has a LICENSE except project-1 to project-5.

## Needs validation before being quoted anywhere

- OncoScan-AI accuracy, Dice and router figures: no evaluation artefacts in the repository.
- All five research projects: CPU-only, few seeds; Elliptic, OSCD/LEVIR-CD, DIV2K runs not done.
- "System remains in daily use" (internship) and CodeChef/LeetCode counts are taken from the resume.
