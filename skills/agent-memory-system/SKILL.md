---
name: product-ship-system
description: End-to-end operating system for discovering, building, validating, and shipping user-loved Next.js products with business outcomes. Use this skill whenever the user asks to build/launch a SaaS, MVP, web app, Next.js product, or wants “idea to deployment” execution, PMF-oriented planning, growth loops, user research synthesis, go-to-market sequencing, or post-launch iteration. Trigger even when the user only says “build this and ship it” or “I want a product users love.”
---

# Product Ship System (Next.js)

This skill turns product intent into shipped outcomes.

Core principle: optimize for **user value + business signal**, not feature volume.

## Mission Profile

Use this workflow when tasks involve any of:
- 0→1 product creation
- MVP scoping and launch
- Next.js full-stack implementation decisions
- deployment + release readiness
- post-launch metrics and iteration

## Operating Mode

Run in phases. Do not skip phase gates.

1. Discover
2. Define
3. Design
4. Build
5. Validate
6. Ship
7. Iterate

If the user asks for “just code now”, still run a compressed Discover+Define pass in 5-10 minutes.

## Persistence Rule (Mandatory)

After user confirms direction (e.g., "go", "I choose X", "start"), immediately persist to filesystem:

- `projects/<project-slug>/00-mission.md`
- `projects/<project-slug>/01-decisions.md`
- `projects/<project-slug>/02-mvp-spec.md`

Append every major decision change with timestamp in `01-decisions.md`.

## DoD Rule (Mandatory)

Each phase must define **Definition of Done (DoD)** before execution. A phase is complete only when its DoD items are met and written in project files.

---

## Phase 1 — Discover (Real Problem Check)

Goal: verify this problem is painful and frequent enough.

### Inputs
- user segment hypothesis
- pain hypothesis
- current alternatives

### Actions
- classify pain: acute / chronic / nice-to-have
- frequency score: daily / weekly / monthly / rare
- willingness proxy: does user already spend time/money workaround?

### Output format
- Problem Statement (1 sentence)
- ICP (ideal customer profile)
- Top 3 existing alternatives
- Why now
- Kill criteria

### Gate
Proceed only if at least 2 of 3 hold:
- pain is acute or chronic
- frequency is weekly+
- clear willingness proxy exists

Use checklist: `checklists/discover.md`

---

## Phase 2 — Define (MVP Spec)

Goal: shrink scope to fastest value loop.

### Actions
- define one north-star outcome
- choose one primary user journey
- limit MVP to 3 must-have capabilities
- explicitly reject non-MVP features

### Output format (strict)
1. North-star outcome
2. User story (single primary)
3. MVP features (max 3)
4. Non-goals
5. Success metrics (activation, retention proxy, conversion proxy)

Template: `templates/mvp-spec.md`

### Gate
No build begins unless:
- MVP <= 3 capabilities
- success metrics are measurable
- non-goals documented

---

## Phase 3 — Design (Experience + Conversion)

Goal: design for clarity and first-value speed.

### Actions
- map first 5 minutes UX
- remove friction in onboarding
- draft landing message: pain → promise → proof → CTA
- define empty/error/loading states before polishing UI

### Output
- User flow map
- Wire-level screen list
- Copy skeleton for Landing/Pricing/Onboarding

Reference: `references/ux-principles.md`

---

## Phase 4 — Build (Next.js Delivery)

Goal: reliable, fast, maintainable implementation.

### Default stack
- Next.js (App Router) + TypeScript
- Tailwind + shadcn/ui
- Prisma + Postgres (or Supabase)
- Auth (Clerk or NextAuth)
- Billing (Stripe)
- Analytics (PostHog/Umami)
- Errors (Sentry)

### Build order
1. data model + auth
2. core user workflow API + UI
3. onboarding + settings
4. pricing/paywall
5. analytics + error capture

### Engineering standards
- schema validation for all external inputs
- typed API contracts
- consistent error boundaries
- no silent failures

Reference: `references/nextjs-architecture.md`

---

## Phase 5 — Validate (Before Ship)

Goal: block bad launches.

### Required checks
- typecheck + lint + build pass
- critical path manual test
- basic performance sanity (LCP/TTFB directionally acceptable)
- analytics events firing
- payment test flow works end-to-end

### Critical paths (minimum)
- signup/login
- primary value action
- checkout
- return session

Checklist: `checklists/pre-ship.md`

---

## Phase 6 — Ship (Controlled Release)

Goal: release safely with rollback confidence.

### Actions
- deploy preview and verify
- promote to production
- verify env vars and external integrations
- record release notes + rollback steps

### Output format
- Production URL
- What shipped
- Known limitations
- Rollback procedure
- 24h watch metrics

Template: `templates/ship-report.md`

---

## Phase 7 — Iterate (PMF Learning Loop)

Goal: learn faster than competitors.

### First 14 days
- collect qualitative feedback (calls/chat/interviews)
- inspect activation drop-offs
- rank issues by impact × confidence × effort
- run 1-2 focused experiments/week

### Iteration rule
Never run more than one major product hypothesis at the same time.

Template: `templates/iteration-log.md`

---

## Phase Artifact Map (Mandatory)

Persist phase outputs under `projects/<project-slug>/`:
- `00-mission.md` (Discover)
- `01-decisions.md` (all phases, append-only)
- `02-mvp-spec.md` (Define)
- `03-design.md` (Design)
- `04-build-log.md` (Build)
- `05-validate-report.md` (Validate)
- `06-ship-report.md` (Ship)
- `07-iteration-log.md` (Iterate)

## Gate Fail Protocol (Mandatory)

If any phase gate fails, do not continue blindly. Output:
1. Failed gate + evidence
2. Minimal fix options (max 3)
3. Recommended option
4. Decision required? (yes/no)

Then pause progression until resolved.

## Constraints Block (Mandatory)

Before Build, explicitly record in project files:
- Timebox (default: 7 days for MVP)
- Budget cap (default: user-specified; if missing, ask once)
- Team mode (solo / agent-only / hybrid)
- Risk tolerance (low/medium/high)

## Risk Review (Mandatory pre-Ship)

Check and record:
- Privacy/compliance concerns
- Third-party dependency risk (auth/payment/API)
- Cost explosion risk (tokens, infra, APIs)
- Abuse/fraud vectors
- Rollback readiness

Use checklist: `checklists/risk-review.md`

## Sub-agent Execution Contract

When parallelizing, each sub-agent task must include:
- Objective
- Inputs
- Output file paths
- Definition of done
- Time budget
- Escalation conditions

Template: `templates/subagent-task.md`

## Phase DoD (Definition of Done)

### Discover DoD
- ICP, pain, alternatives, why-now, kill criteria documented
- Gate condition satisfied (>=2/3 criteria)

### Define DoD
- North-star, single primary story, max-3 MVP features finalized
- Non-goals and success metrics documented

### Design DoD
- First-5-minute flow mapped
- Screen list + conversion copy skeleton drafted

### Build DoD
- Core workflow implemented end-to-end
- Auth/data/payment/analytics paths integrated for MVP scope

### Validate DoD
- typecheck/lint/build pass
- Critical path checks complete
- Observability and payment flows verified

### Ship DoD
- Production deployment completed
- Ship report with rollback and watch metrics delivered

### Iterate DoD
- Feedback and behavioral signals logged
- Next experiment selected with hypothesis + metric target

## Decision Heuristics

### Build vs Cut
Cut any feature that fails one of:
- directly improves north-star outcome
- requested by multiple target users
- needed for core loop completion

### Speed vs Quality
- Internal logic/data integrity: quality first
- UI polish before signal: speed first

### Ask user only at critical gates
Escalate only for:
- strategy conflict
- legal/compliance/financial risk
- production launch approval (if not pre-authorized)

---

## Tool and Skill Orchestration Guidance

Use specialized skills/tools where available:
- UI quality work → frontend-design
- deployment to Vercel → vercel-deploy / vercel-cli
- deep market/domain synthesis → deep-research
- web workflow verification → webapp-testing

Use parallel/sub-agent execution for:
- code generation across modules
- test writing + execution
- docs and release notes prep

Keep main thread focused on decisions and milestone summaries.

---

## Anti-Patterns (Do Not Do)

- feature stuffing before first user signal
- equating launch with PMF
- optimizing architecture while value proposition is unproven
- vanity metrics without behavioral signal
- building without explicit kill criteria

---

## Standard Reply Contract to User

For each milestone, report in this exact shape:
1. Current phase
2. What was completed
3. Evidence/metrics
4. Risks/blockers
5. Next action
6. Need decision? (yes/no)

Keep concise, outcome-driven, and decision-ready.
