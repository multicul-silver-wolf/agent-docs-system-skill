# Docs Layout

## Canonical File Set

Use this layout when bootstrapping or repairing a project docs system:

- `AGENTS.md`
  - Keep this as the agent entry point.
  - If `.docs/` is initialized, include the docs-system rules block.
  - If `.docs/` is not initialized, defer adding the block.
- `.docs/DOCS.md`
  - Store cross-domain, durable docs.
- `.docs/index.md`
  - Act as the map for first-level domains.
- `.docs/<domain>/index.md`
  - Act as the map for second-level docs in one domain.
- `.docs/<domain>/<subdomain>.md`
  - Store durable knowledge that only applies to one subdomain.

## AGENTS Rules Block

When `.docs/` is initialized, ensure `AGENTS.md` includes this exact block:

```md
<!-- BEGIN:docs-system-rules -->
# This is NOT the docs you remember

This repository uses a project docs system with a two-level map under `.docs/`.
Read `.docs/index.md` and the relevant `.docs/<domain>/index.md` before writing or updating docs.
If `.docs/` is not initialized yet, initialize it first, then add this rules block.
<!-- END:docs-system-rules -->
```

## Frontmatter

Every docs document should start with frontmatter. When creating a new system, use at least:

```yaml
---
title: Example Title
description: One-line description of what this docs file covers.
updateAt: 2026-03-24
---
```

## File Roles

### `.docs/DOCS.md`

Store:

- durable project-wide terminology
- cross-domain conventions
- recurring user preferences that affect many tasks
- architectural expectations that show up repeatedly

Avoid:

- domain-specific implementation notes
- temporary debugging observations
- one-off task status

### `.docs/index.md`

Include:

- a short usage note
- one entry per first-level domain
- when to consult each domain

### `.docs/<domain>/index.md`

Include:

- a short usage note for that domain
- one entry per `.docs/<domain>/<subdomain>.md`
- when to consult each subdomain doc

### `.docs/<domain>/<subdomain>.md`

Store:

- subdomain-specific conventions
- ownership boundaries
- stable file or route relationships
- user corrections that only matter in that subdomain

Prefer one clear subdomain per file, such as:

- `.docs/frontend/routing.md`
- `.docs/frontend/data-fetching.md`
- `.docs/backend/api-contracts.md`
- `.docs/backend/auth-flow.md`

## Placement Rules

Use this decision rule before writing:

- If knowledge should apply across the repository, put it in `.docs/DOCS.md`.
- If it maps first-level navigation, put it in `.docs/index.md`.
- If it maps second-level navigation, put it in `.docs/<domain>/index.md`.
- If it only matters for one subdomain, put it in `.docs/<domain>/<subdomain>.md`.
- If it is too temporary to help future work, do not store it.

## Update Triggers

Update the relevant docs file when:

- the user corrects the agent
- the user clarifies a stable project convention
- a new module, route, feature, or workflow becomes important enough to remember
- an existing domain or subdomain changes ownership, structure, or boundaries

Also update map files whenever docs files change:

- Update `.docs/<domain>/index.md` when its subdomain files change.
- Update `.docs/index.md` when first-level domains change.
