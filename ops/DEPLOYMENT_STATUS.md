# Deployment status

Last updated: 13 November 2026.

| Application | Target | Status | Evidence |
|---|---|---|---|
| Profile README | github.com/saaki05 | Complete and verified | merged to `main` (d34df45); banner, badges, skill icons and diagram render on GitHub |
| Portfolio site (old) | Vercel, old account | Failed | both URLs return HTTP 402 "deployment paused" |
| Portfolio site (new) | Vercel, new account | Blocked by authentication | new account not connected; site not built yet |
| Chennai dashboard | GitHub Pages | Implemented but not fully verified | page loads; data refresh not confirmed |
| lsmkv CI | GitHub Actions | Complete and verified | run #1 on `distributed` succeeded on Python 3.10, 3.12, 3.13 |

## Planned hosting split (to be confirmed against current free-tier terms before use)

- Static and front-end sites: Vercel (new account) or GitHub Pages. The portfolio site should be a static build so it costs no function invocations.
- Python inference services: not Vercel. Candidates to compare: Hugging Face Spaces, Render, Fly.io, Google Cloud Run.
- Scheduled jobs: GitHub Actions cron, as the Chennai dashboard already does.
- Databases: a hosted Postgres free tier or SQLite on the service's disk.

The free-tier comparison has not been researched yet; no platform has been chosen and nothing paid has been activated.
