# Vercel deployment inventory

Last updated: 13 November 2026. Status: **incomplete — blocked by authentication.**

The Vercel dashboard could not be read: the built-in browser is not signed in to Vercel (`vercel.com/dashboard` redirects to the login page) and no Vercel connector is attached. Project settings, build configuration, environment variable names and deployment history are therefore unknown. Nothing below is guessed.

## Verified from outside

| URL | Source of the link | Result on 13 Nov 2026 | Repository (from README) |
|---|---|---|---|
| portfolio-nine-sable-38.vercel.app | Saaketh-Portfolio README, old profile README | HTTP 402, "This deployment is temporarily paused" | Saaketh-Portfolio (identical copy: saaki-resume-portfolio) |
| portfolio-saaki05s-projects.vercel.app | GitHub profile website field, saaketh05 README | HTTP 402, "This deployment is temporarily paused" | unknown; likely the same project |

## Deployments configured in repositories, not on Vercel

| Repository | Platform | Evidence | State |
|---|---|---|---|
| chennai-insights-dashboard | GitHub Pages | `docs/`, cron workflow | page loads |
| bhoomisetu-app- | Render (Docker) | `render.yaml`, `Dockerfile` | not checked |
| Great-Agent-hackathon- | Render | `render.yaml` | not checked |
| flowforge-chat-proxy | Render | README | not checked |

No `vercel.json` exists in any of the 28 own repositories.

## To complete this inventory

Sign in to the old Vercel account in the Claude desktop app's browser pane (or connect a Vercel connector). Every project's Settings → General, Git, Environment Variables and Deployments tabs will then be read and recorded here. Variable names only; values are never copied.
